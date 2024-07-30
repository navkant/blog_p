from django.urls import include, path

from blog.blog_content.presentation import views


urlpatterns = [
    path(r"", views.ListAllBlogsView.as_view(), name="list_all_views"),
    path(r"<int:blog_id>/", views.GetBlogView.as_view(), name="get-blog"),
    path(r"user/", views.ListUserBlogsView.as_view(), name='user-blogs'),
]
