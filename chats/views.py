from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Messages, Chat
from .serializers import ChatSerializer, MessagesSerializer
from rest_framework.response import Response


class Chats(GenericAPIView):
    '''
        Chats home page
    '''

    def get(self, request):
        return render(request, 'chats/chats.html')


class ChatView(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializers = ChatSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Your chat created successfully'}, 201)

        return Response(f"{serializers.errors}", 400)

    def get(self, request):
        user = request.GET.get('user')
        return Chat.objects.filter(owner=request.user, user=user)


class MessageView(ListCreateAPIView):
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializers = MessagesSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Your message created successfully'}, 201)

        return Response(f"{serializers.errors}", 400)

    def get(self, request):
        user = request.GET.get('user')
        return Messages.objects.filter(chat__owner=request.user, chat__user=user)
