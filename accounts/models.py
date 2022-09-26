from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, phone_number, password, email=None):
        '''
        Create a CustomUser with username, name, password and other extra fields
        '''

        now = timezone.now()

        if email:
            email = CustomUserManager.normalize_email(email)

        cuser = self.model(username=username, email=email, first_name=first_name, last_name=last_name,
                           phone_number=phone_number, is_staff=False, is_active=True, is_superuser=False,
                           date_joined=now, last_login=now,)
        cuser.set_password(password)
        cuser.save(using=self._db)
        return cuser

    def create_superuser(self, username, first_name, last_name, phone_number, password, email=None):
        u = self.create_user(username, first_name, last_name, phone_number, password, email)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)

        return u


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_validator = RegexValidator(regex=r'^(0|\+?98)9\d{9}$')
    phone_number = models.CharField(max_length=15, validators=[phone_validator], unique=True)
    avatar = models.ImageField()

    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]
