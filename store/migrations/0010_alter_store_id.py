# Generated by Django 3.2.9 on 2021-11-23 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.UUID('909ec5c0-0edc-5f0b-8723-64d1b429dae7'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
