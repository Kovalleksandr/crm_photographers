# apps/accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from apps.multi_tenancy.models import Organization  # Додаємо імпорт

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Адміністратор'),
        ('photographer', 'Фотограф'),
        ('retoucher', 'Ретушер'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='photographer')
    organization = models.ForeignKey(
        'multi_tenancy.Organization',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )

    def save(self, *args, **kwargs):
        if self.role == 'admin' and not self.organization and not self.pk:
            super().save(*args, **kwargs)
            org = Organization.objects.create(name=f"Org_{self.username}", owner=self)
            self.organization = org
            super().save(update_fields=['organization'])
        else:
            super().save(*args, **kwargs)

class Invitation(models.Model):
    code = models.CharField(max_length=16, unique=True, default=get_random_string)
    organization = models.ForeignKey(
        'multi_tenancy.Organization',
        on_delete=models.CASCADE,
        related_name='invitations'
    )
    role = models.CharField(max_length=20, choices=CustomUser.ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)