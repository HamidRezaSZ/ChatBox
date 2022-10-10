from rest_framework import serializers
from .models import Chat, Messages
from accounts.models import User


class UserOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'avatar')


class ChatSerializer(serializers.ModelSerializer):
    owner = UserOwnerSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ('owner',)


class MessagesSerializer(serializers.ModelSerializer):
    '''
        Messages serializers
    '''

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    username = serializers.CharField(write_only=True)
    chat = ChatSerializer(read_only=True)

    class Meta:
        model = Messages
        fields = ('created_at', 'chat', 'message', 'username')

    def create(self, validated_data):
        user = self.context.get('user')
        username = User.objects.get(username=validated_data['username'])

        chat_obj, created = Chat.objects.get_or_create(owner=user, user=username)

        obj = Messages.objects.create(chat=chat_obj, message=validated_data['message'])

        return obj
