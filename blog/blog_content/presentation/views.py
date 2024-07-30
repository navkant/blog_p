from dependency_injector.wiring import Provide
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status

from blog.blog_content.domain.usecases.list_all_blogs_usecase import ListAllBlogsUsecase
from blog.blog_content.presentation.types import BlogResponseList


class ListAllBlogs(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request, list_all_blogs_use_case: ListAllBlogsUsecase = Provide["blog_container.list_all_blogs_use_case"]):
        blogs = list_all_blogs_use_case.execute()

        return Response(
            BlogResponseList.from_orm(blogs).dict(), status=status.HTTP_200_OK
        )