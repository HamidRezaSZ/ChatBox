from django.urls import path
from .views import ChatView, Chats, MessageView

app_name = "chats"

urlpatterns = [
    path('', Chats.as_view(), name='chats_home'),  # chats home page
    path('chat/create/', ChatView.as_view(), name='create_chat'),  # create chat
    path('message/create/', MessageView.as_view(), name='create_message'),  # create message
]
