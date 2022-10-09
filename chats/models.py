from django.db import models
from accounts.models import User


class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')


class Messages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
