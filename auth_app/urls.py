from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PasswordChangeView

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("auth/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/change-password/", PasswordChangeView.as_view(), name="change_password"),
]
