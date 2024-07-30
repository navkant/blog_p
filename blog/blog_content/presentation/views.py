from dependency_injector.wiring import Provide
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from blog.blog_content.domain.usecases.list_all_blogs_usecase import ListAllBlogsUsecase
from blog.blog_content.domain.usecases.get_blog_usecase import GetBlogUsecase
from blog.blog_content.domain.usecases.list_user_blogs_usecase import ListUserBlogs
from blog.blog_content.presentation.types import BlogResponseList


class ListAllBlogsView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, list_all_blogs_use_case: ListAllBlogsUsecase = Provide["blog_container.list_all_blogs_use_case"]):
        blogs = list_all_blogs_use_case.execute()

        return Response(
            BlogResponseList.from_orm(blogs).model_dump(), status=status.HTTP_200_OK
        )


class GetBlogView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, blog_id: int, get_blog_use_case: GetBlogUsecase = Provide["blog_container.get_blog_use_case"]):
        blog = get_blog_use_case.execute(blog_id=blog_id)

        return Response(
            blog.model_dump(), status=status.HTTP_200_OK
        )


class ListUserBlogsView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, list_user_blogs: ListUserBlogs = Provide["blog_container.list_user_blogs"]):
        blogs = list_user_blogs.execute(user_id=request.user.id)

        return Response(blogs.model_dump(), status=status.HTTP_200_OK)


class UpdateBlogView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        pass