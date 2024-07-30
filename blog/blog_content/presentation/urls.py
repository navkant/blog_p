from django.urls import include, path

from blog.blog_content.presentation import views


urlpatterns = [
    path(r"", views.ListAllBlogs.as_view(), name="list_all_views"),
    path(r"<int:blog_id>/", views.GetBlog.as_view(), name="get-blog"),
]
