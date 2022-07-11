from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.db.models import Q

import datetime

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email: str, password: str) -> 'CustomUser':
        if not email:
            raise ValidationError('Email required')
        
        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    

    def create_superuser(self, email: str, password: str):
        if not email:
            raise ValidationError('Email required')
        
        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    

    def get_staff_from_date_joined(self):
        managers = self.filter(Q(is_staff=True) & Q(date_joined__gte=datetime.date(2022, 6, 1)))
        return managers

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Почта/Логин', unique=True
    )
    phone_number = PhoneNumberField(
        'Номер телефона'
    )
    image = models.ImageField(
        'Фото профиля', default=None, null=True
    )
    is_active = models.BooleanField(
        'Активность',
        default=True
    )
    is_staff = models.BooleanField(
        'Статус менеджера',
        default=False
    )
    date_joined = models.DateField(
        'Время создания',
        default=timezone.now
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'