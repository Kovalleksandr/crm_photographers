# apps/multi_tenancy/models.py
from django.db import models
from .utils import create_database

class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='owned_organizations'
    )
    db_name = models.CharField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Нова організація
            # Спочатку визначаємо db_name перед збереженням
            self.db_name = f"tenant_{self.id or Organization.objects.count() + 1}"
            super().save(*args, **kwargs)  # Зберігаємо з уже заповненим db_name
            create_database(self.db_name)
        else:
            super().save(*args, **kwargs)