from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=64, null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    birth_date = models.DateField(null=True)

    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
