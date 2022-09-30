from rest_framework import serializers
from .models import Chat, Messages


class ChatSerializer(serializers.ModelSerializer):
    '''
        Chat serializers
    '''

    class Meta:
        model = Chat
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    '''
        Messages serializers
    '''

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Messages
        fields = '__all__'
