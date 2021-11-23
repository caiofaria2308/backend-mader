# Generated by Django 3.2.9 on 2021-11-23 18:17

from django.db import migrations, models
import django_cpf_cnpj.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='document_number',
        ),
        migrations.AddField(
            model_name='client',
            name='document_cnpj',
            field=django_cpf_cnpj.fields.CNPJField(max_length=18, null=True, unique=True, verbose_name='cnpj'),
        ),
        migrations.AddField(
            model_name='client',
            name='document_cpf',
            field=django_cpf_cnpj.fields.CPFField(max_length=14, null=True, unique=True, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bec248c5-98a3-5b02-a76a-4f5cf0fa4aaf'), primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
