"""
URL configuration for blog_p project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from blog import urls as blog_urls
from basic_token_auth.views import GetAuthToken, RefreshAuthToken
from blog.blog_content.presentation import urls as blog_urls_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include(blog_urls)),
    path(r"v2/blogs/", include(blog_urls_v2)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')

    # path(r'api_token_auth/', GetAuthToken.as_view(), name='get_auth_token'),
    # path(r'refresh_auth_token/', RefreshAuthToken.as_view(), name='refresh_auth_token'),
]
