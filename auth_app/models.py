from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, role=None, enabled=True):
        if not username:
            raise ValueError("The username must be set")
        user = self.model(username=username, role=role, enabled=enabled)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        return self.create_user(
            username=username, password=password, role="admin", enabled=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.username
