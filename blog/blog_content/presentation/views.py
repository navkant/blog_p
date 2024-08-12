from dependency_injector.wiring import Provide
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from blog.blog_content.domain.domain_models import BlogUpdateRequestDomainModel
from blog.blog_content.domain.domain_models import BlogCreateDomainModel
from blog.blog_content.domain.usecases.create_blog_usecase import CreateBlogUsecase
from blog.blog_content.domain.usecases.list_all_blogs_usecase import ListAllBlogsUsecase
from blog.blog_content.domain.usecases.get_blog_usecase import GetBlogUsecase
from blog.blog_content.domain.usecases.list_user_blogs_usecase import ListUserBlogs
from blog.blog_content.domain.usecases.update_blog_usecase import UpdateBlogUsecase
from blog.blog_content.presentation.types import BlogResponseList, BlogResponse, BlogUpdateRequesst
from time import perf_counter


class ListAllBlogsView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, list_all_blogs_use_case: ListAllBlogsUsecase = Provide["blog_container.list_all_blogs_use_case"]):
        t1_start = perf_counter()
        blogs = list_all_blogs_use_case.execute()
        t1_stop = perf_counter()
        print("Elapsed time during the whole program in seconds:", t1_stop - t1_start)
        return Response(
            BlogResponseList.from_orm(blogs).model_dump(), status=status.HTTP_200_OK
        )


class GetUpdateBlogView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, blog_id: int, get_blog_use_case: GetBlogUsecase = Provide["blog_container.get_blog_use_case"]):
        blog = get_blog_use_case.execute(blog_id=blog_id)
        blog_response = BlogResponse.model_validate(blog)

        return Response(
            blog_response.model_dump(), status=status.HTTP_200_OK
        )

    def patch(self, request, blog_id: int, update_blog_usecase: UpdateBlogUsecase = Provide["blog_container.update_blog_use_case"]):
        blog_update_request = BlogUpdateRequesst.parse_obj(request.data)
        blog_update_request_domain_model = BlogUpdateRequestDomainModel(
            blog_id=blog_id,
            content=blog_update_request.content
        )
        blog_response = update_blog_usecase.execute(blog_update_request=blog_update_request_domain_model)

        return Response(
            blog_response.model_dump(), status=status.HTTP_200_OK
        )


class ListUserBlogsView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, list_user_blogs: ListUserBlogs = Provide["blog_container.list_user_blogs_use_case"]):
        blogs = list_user_blogs.execute(user_id=request.user.id)

        return Response(BlogResponseList.from_orm(blogs).model_dump(), status=status.HTTP_200_OK)


class CreateBlogView(APIView):
    # permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request, create_blog_usecase: CreateBlogUsecase = Provide["blog_container.create_blog_use_case"]):
        blog_create_request = BlogCreateDomainModel.model_validate(request.data)
        blog = create_blog_usecase.execute(blog_create_request=blog_create_request)
        blog_response = BlogResponse.model_validate(blog)

        return Response(
            blog_response.model_dump(), status=status.HTTP_200_OK
        )
