# Generated by Django 5.1.4 on 2025-01-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.IntegerField(),
        ),
    ]