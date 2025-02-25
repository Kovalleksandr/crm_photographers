# apps/accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Адміністратор'),
        ('photographer', 'Фотограф'),
        ('retoucher', 'Ретушер'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='photographer')
    organization = models.ForeignKey(
        'multi_tenancy.Organization',  # Оновлено шлях із 'multi_tenancy' на 'apps.multi_tenancy'
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