# Generated by Django 3.2.9 on 2021-11-23 15:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.UUID('23ad76be-d2e1-4dbf-8702-29d4361e5dac'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]