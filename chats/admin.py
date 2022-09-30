from django.contrib import admin
from .models import Messages, Chat


class MessagesInline(admin.TabularInline):
    model = Messages


@admin.register(Chat)
class ChatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'user')
    inlines = (MessagesInline,)
