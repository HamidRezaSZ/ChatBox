from django.shortcuts import render
from rest_framework.generics import GenericAPIView


class Chats(GenericAPIView):
    '''
        Chats home page
    '''

    def get(self, request):
        return render(request, 'chats/chats.html')
