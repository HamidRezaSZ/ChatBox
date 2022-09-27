from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


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


class Login(CreateAPIView):
    def get(self, request):
        return render(request, 'accounts/login.html')


class Logout(GenericAPIView):
    '''
        Logout users with block token with jwt.
    '''

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({'detail': 'Token is invalid or expired'}, status=status.HTTP_400_BAD_REQUEST)
