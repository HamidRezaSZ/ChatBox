from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer


class Register(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user_serializers = UserSerializer(data=request.data)
        if user_serializers.is_valid():
            user_serializers.save()
            return Response({'message': 'User created successfully!'})

        return Response({'message': user_serializers.errors})

    def get(self, request):
        return render(request, 'accounts/register.html')
