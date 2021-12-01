# Generated by Django 3.2.9 on 2021-12-01 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_responsable_deliverysubway_responsible'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverysubway',
            name='delivered_hour',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='hora de entrega'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliverysubway',
            name='delivered_date',
            field=models.DateField(verbose_name='data de entrega'),
        ),
    ]
