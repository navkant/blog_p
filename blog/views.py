from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import response, status

from blog.domain_models import BlogDomainModel, BlogListDomainModel
from rest_framework.permissions import IsAuthenticated
from blog.models import Blog


class ListAllBlogs(APIView):

    def get(self, request):
        blogs = Blog.objects.all().order_by("-id")
        blogs = BlogListDomainModel(items=list(map(BlogDomainModel.from_orm, blogs)))

        return response.Response(blogs.dict(), status=status.HTTP_200_OK)


class GetBlog(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        return response.Response(BlogDomainModel.from_orm(blog).dict(), status=status.HTTP_200_OK)


class ListUserBlogs(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.filter(author=request.user).order_by("-id")
        blogs = BlogListDomainModel(items=list(map(BlogDomainModel.from_orm, blogs)))

        return response.Response(blogs.dict(), status=status.HTTP_200_OK)
