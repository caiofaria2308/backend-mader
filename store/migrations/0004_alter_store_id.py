# Generated by Django 3.2.9 on 2021-11-23 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0c7ff172-0f47-5af3-bde9-09a0208c4b78'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]