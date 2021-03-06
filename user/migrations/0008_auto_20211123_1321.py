# Generated by Django 3.2.9 on 2021-11-23 16:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f696d0d7-8c82-57d7-becc-de10591278af'), primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.type', verbose_name='tipo'),
        ),
    ]
