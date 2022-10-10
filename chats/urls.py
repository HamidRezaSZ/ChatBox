from django.urls import path
from .views import Chats, MessageView
from django.contrib.auth.decorators import login_required

app_name = "chats"

urlpatterns = [
    path('', login_required(Chats.as_view()), name='chats_home'),  # chats home page
    path('message/', login_required(MessageView.as_view()), name='message'),  # create/get message
]
