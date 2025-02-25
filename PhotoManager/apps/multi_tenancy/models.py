# apps/multi_tenancy/models.py
from django.db import models
from .utils import create_database

class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'accounts.CustomUser',  # Оновлено шлях із 'accounts' на 'apps.accounts'
        on_delete=models.CASCADE,
        related_name='owned_organizations'
    )
    db_name = models.CharField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.db_name = f"tenant_{self.id}"
            create_database(self.db_name)
            super().save(update_fields=['db_name'])
        else:
            super().save(*args, **kwargs)