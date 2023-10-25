from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from users.constants import Role
from users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    role = models.CharField(
        max_length=2, default=Role.JUNIOR
    )  # TODO: constants choices=Role.values()

    objects = UserManager()

    EMAIL_FIELD = (
        "email"  # email = models.EmailField(max_length=255, unique=True)
    )
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


# class Role(models.Model):
#     ROLES = [
#         ('ADMIN', 'admin'),
#         ('JUNIOR', 'junior'),
#         ('OPERATOR', 'operator')
#     ]
#     value = models.CharField(max_length=10,
#                              choices=ROLES,
#                              default='JUNIOR')
#
#     def __str__(self):
#         return self.value


#
# class User(models.Model):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
