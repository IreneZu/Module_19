# Generated by Django 5.1.4 on 2025-01-03 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='age',
            new_name='description',
        ),
    ]