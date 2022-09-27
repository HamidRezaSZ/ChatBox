from django.urls import path
from .views import Register
from .views import Logout, Login
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

app_name = "accounts"

urlpatterns = [
    path('register/', Register.as_view(), name='register'),  # register user
    path('login/', Login.as_view(), name='login'),  # login user

    # JWTAuthentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # get jwt token
    path('logout/', Logout.as_view(), name='logout'),  # user logout with jwt
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # jwt refresh token
]
