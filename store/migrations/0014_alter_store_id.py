# Generated by Django 3.2.9 on 2021-11-24 11:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.UUID('49fca79b-e366-57ad-9014-0e51cbe217dd'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
