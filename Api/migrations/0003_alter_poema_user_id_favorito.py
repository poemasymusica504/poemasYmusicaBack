# Generated by Django 4.2.4 on 2024-06-16 01:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_remove_usuario_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poema',
            name='user_id_favorito',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=[], size=None),
        ),
    ]