import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from users.constants import Role
from users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    username = None  # TODO: does it look good???
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    role = models.CharField(
        max_length=2, default=Role.JUNIOR, choices=Role.values()
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.email


class ActivationKey(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
