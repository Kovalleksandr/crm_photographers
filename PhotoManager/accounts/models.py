from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Адміністратор'),
        ('photographer', 'Фотограф'),
        ('retoucher', 'Ретушер'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='photographer')
