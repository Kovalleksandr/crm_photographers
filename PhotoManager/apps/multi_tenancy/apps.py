# apps/multi_tenancy/apps.py
from django.apps import AppConfig

class MultiTenancyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.multi_tenancy'  # Повне ім’я застосунку
