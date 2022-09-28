from django.urls import path
from .views import Register, Logout
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

app_name = "accounts"

urlpatterns = [
    path('register/', Register.as_view(), name='register'),  # register user

    # JWTAuthentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # get jwt token
    path('logout/', Logout.as_view(), name='logout'),  # user logout with jwt
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # jwt refresh token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # verify jwt token
]
