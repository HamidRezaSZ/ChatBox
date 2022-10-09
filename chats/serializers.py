from rest_framework import serializers
from .models import Chat, Messages


class MessagesSerializer(serializers.ModelSerializer):
    '''
        Messages serializers
    '''

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    username = serializers.CharField(write_only=True)
    chat = serializers.CharField(read_only=True)

    class Meta:
        model = Messages
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('user')

        chat_name = Chat.objects.get_or_create(owner=user, user=validated_data['username'])

        obj = Messages.objects.create(chat=chat_name, message=validated_data['message'])

        return obj
