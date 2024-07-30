from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from blog.domain_models import BlogDomainModel, BlogListDomainModel, UserDetails
from rest_framework.permissions import IsAuthenticated
from blog.models import Blog


class ListAllBlogs(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        blogs = Blog.objects.all().order_by("-id")
        blogs = BlogListDomainModel(items=list(map(BlogDomainModel.from_orm, blogs)))

        return response.Response(blogs.dict(), status=status.HTTP_200_OK)


class GetBlog(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        return response.Response(BlogDomainModel.from_orm(blog).dict(), status=status.HTTP_200_OK)


class ListUserBlogs(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        blogs = Blog.objects.filter(author=request.user).order_by("-id")
        blogs = BlogListDomainModel(items=list(map(BlogDomainModel.from_orm, blogs)))

        return response.Response(blogs.dict(), status=status.HTTP_200_OK)


class GetUserDetails(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        user_details = {
            "id": request.user.id,
            "email": request.user.email,
            "username": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name
        }
        return response.Response(UserDetails.parse_obj(user_details).dict(), status=status.HTTP_200_OK)


class CreateBlog(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        pass
