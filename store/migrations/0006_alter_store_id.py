# Generated by Django 3.2.9 on 2021-11-23 16:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.UUID('df89226a-45e5-59cc-9c7d-97a6f95654f0'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]