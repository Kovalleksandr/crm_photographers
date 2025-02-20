from django.db import models
from django.contrib.auth import get_user_model
from .utils import create_database

User = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        При створенні організації автоматично створюємо базу даних.
        """
        if not self.pk:  # Якщо це новий об'єкт
            super().save(*args, **kwargs)
            db_name = f"org_{self.id}"
            create_database(db_name)

# Create your models here.
