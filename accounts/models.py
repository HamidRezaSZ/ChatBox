from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, phone_number):
        '''
        Create a CustomUser with username, name, password and other extra fields
        '''

        now = timezone.now()

        cuser = self.model(username=username, phone_number=phone_number, is_staff=False,
                           is_active=True, is_superuser=False, date_joined=now, last_login=now,)
        cuser.set_password(password)
        cuser.save(using=self._db)
        return cuser

    def create_superuser(self, username, password, phone_number):
        u = self.create_user(username, password, phone_number)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)

        return u


class User(AbstractUser):
    phone_validator = RegexValidator(regex=r'^(0|\+?98)9\d{9}$')
    phone_number = models.CharField(max_length=15, validators=[phone_validator], unique=True, blank=True, null=True)
    avatar = models.ImageField()
