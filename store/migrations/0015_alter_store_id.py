# Generated by Django 3.2.9 on 2021-11-24 12:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
