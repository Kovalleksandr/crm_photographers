import os
from django.conf import settings
from django.db import connection
from django.core.management import call_command

def create_database(db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE {db_name};")

    # Копіюємо всю конфігурацію 'default' і змінюємо тільки 'NAME'
    settings.DATABASES[db_name] = settings.DATABASES['default'].copy()
    settings.DATABASES[db_name]['NAME'] = db_name

    call_command('migrate', database=db_name)