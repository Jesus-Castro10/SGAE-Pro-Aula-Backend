from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')
        
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('admin', 'admin'),
    )
    
    username = models.CharField(
        'nombre de usuario',
        max_length=30,
        unique=True
    )
    
    user_type = models.CharField(
        'tipo de usuario',
        max_length=20,
        choices=USER_TYPE_CHOICES
    )
    
    is_active = models.BooleanField(
        'activo',
        default=True
    )
    
    is_staff = models.BooleanField(
        'acceso admin',
        default=False
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_type']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'