# Generated by Django 4.0 on 2024-06-11 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='admin',
        ),
    ]