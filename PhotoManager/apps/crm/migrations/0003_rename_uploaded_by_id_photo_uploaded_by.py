# Generated by Django 5.1.6 on 2025-03-14 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_rename_uploaded_by_photo_uploaded_by_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='uploaded_by_id',
            new_name='uploaded_by',
        ),
    ]
