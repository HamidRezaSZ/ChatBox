from django.urls import path
from .views import Login, Register, Logout
from django.contrib.auth.decorators import login_required

app_name = "accounts"

urlpatterns = [
    path('register/', Register.as_view(), name='register'),  # register user
    path('logout/', login_required(Logout.as_view()), name='logout'),  # user logout
    path('login/', Login.as_view(), name='token_obtain_pair'),  # user login
]
