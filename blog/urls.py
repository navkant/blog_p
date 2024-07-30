from django.urls import path

from blog import views
from blog.blog_content.presentation import urls as blog_urls_v2
from django.urls import include


urlpatterns = [
    path(r"", views.ListAllBlogs.as_view(), name="list-blogs"),
    path(r"<int:id>/", views.GetBlog.as_view(), name="get-blog"),
    path(r"user/", views.ListUserBlogs.as_view(), name="user-blogs"),
    path(r"user/details/", views.GetUserDetails.as_view(), name="user-details")
]
