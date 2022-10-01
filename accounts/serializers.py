from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from disposable_email_domains import blocklist


class UserSerializer(serializers.ModelSerializer):
    '''
        User serializers for register
    '''

    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "phone_number", "password", "password2")

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        elif validated_data['email'].split('@')[1] in blocklist:
            raise serializers.ValidationError({"email": "The email domain is blocked."})

        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
