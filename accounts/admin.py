from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from accounts.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {
             'fields':
             ('avatar', 'first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active')
    list_editable = ('is_staff', 'is_active')
