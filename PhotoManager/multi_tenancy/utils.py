import os
from django.conf import settings
from django.db import connection
from django.core.management import call_command

def create_database(db_name):
    """
    Створює нову базу даних для команди.
    """
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE {db_name};")

    settings.DATABASES[db_name] = {
        'ENGINE': 'django.db.backends.postgresql',  # Або інший, якщо MySQL
        'NAME': db_name,
        'USER': settings.DATABASES['default']['USER'],
        'PASSWORD': settings.DATABASES['default']['PASSWORD'],
        'HOST': settings.DATABASES['default']['HOST'],
        'PORT': settings.DATABASES['default']['PORT'],
    }

    call_command('migrate', database=db_name)
