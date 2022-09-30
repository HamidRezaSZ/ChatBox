from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .serializers import LoginSerializers, UserSerializer
from rest_framework.generics import GenericAPIView


class Home(GenericAPIView):

    def get(self, request):
        return render(request, 'accounts/index.html')


class Register(CreateAPIView):
    '''
        Register users
    '''

    serializer_class = UserSerializer

    def post(self, request):
        user_serializers = UserSerializer(data=request.data)
        if user_serializers.is_valid():
            user_serializers.save()
            return Response({'message': 'User created successfully!'}, status=201)

        return Response({"message": f"{user_serializers.errors}"}, status=400)


class Login(GenericAPIView):
    '''
        Login users.
    '''

    serializer_class = LoginSerializers

    def post(self, request):
        serializers = LoginSerializers(data=request.data)

        if serializers.is_valid():
            user = authenticate(request, username=serializers.data['username'], password=serializers.data['password'])
            if user is not None:
                login(request, user)
                return Response({'message': 'Logged in successfully!'}, status=200)

            return Response('Username or password is incorrect !', 400)

        return Response({"message": f"{serializers.errors}"}, status=400)


class Logout(GenericAPIView):
    '''
        Logout users.
    '''

    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("home"))
