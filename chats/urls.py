from django.urls import path

from chats.views import Chats

app_name = "chats"

urlpatterns = [
    path('', Chats.as_view(), name='chats_home'),  # chats home page
]
