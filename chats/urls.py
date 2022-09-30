from django.urls import path
from .views import ChatView, Chats, MessageView
from django.contrib.auth.decorators import login_required

app_name = "chats"

urlpatterns = [
    path('', login_required(Chats.as_view()), name='chats_home'),  # chats home page
    path('chat/create/', login_required(ChatView.as_view()), name='create_chat'),  # create chat
    path('message/create/', login_required(MessageView.as_view()), name='create_message'),  # create message
]
