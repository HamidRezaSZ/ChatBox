from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


class Chats(GenericAPIView):
    '''
        Chats home page
    '''

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        return render(request, 'chats/chats.html')
