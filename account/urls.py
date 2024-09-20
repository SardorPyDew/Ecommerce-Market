from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import LogOutView, RegisterView

app_name = "account"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="signin"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogOutView.as_view(), name="token_refresh"),
]