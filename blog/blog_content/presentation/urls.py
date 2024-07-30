from django.urls import include, path

from blog.blog_content.presentation import views


urlpatterns = [
    path(r"", views.ListAllBlogs.as_view(), name="list_all_views"),
]