# Generated by Django 3.2.9 on 2021-11-23 18:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20211123_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.UUID('03b8a3d2-84c8-53b9-88db-54508364e987'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
