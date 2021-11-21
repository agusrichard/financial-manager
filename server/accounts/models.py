from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=64, null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    birth_date = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return f'Account(' \
               f'email={self.email}, ' \
               f'full_name={self.full_name}, ' \
               f'is_active={self.is_active}, ' \
               f'date_joined={self.date_joined}, ' \
               f'is_deleted={self.is_deleted}, ' \
               f'birth_date={self.birth_date}' \
               f')'
