from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from users.views import CustomTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]