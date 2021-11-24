from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField
import uuid


class Client(models.Model):
    DOCUMENTS_TYPE = (
        ("CPF", "CPF"),
        ("CNPJ", "CNPJ")
    )
    id = models.UUIDField(
        verbose_name="id",
        primary_key=True,
        default=uuid.uuid4
    )
    created_at = models.DateTimeField(
        verbose_name="data de criação",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="data de atualização",
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name="se cliente está ativo",
        default=True
    )
    
    name = models.CharField(
        verbose_name="nome",
        max_length=256
    )
    document_type = models.CharField(
        verbose_name="tipo do documento",
        max_length=5,
        choices=DOCUMENTS_TYPE,
        null=True
    )
    
    document_cpf = CPFField(
        verbose_name="cpf",
        null=True,
        unique=True
    )
    document_cnpj = CNPJField(
        verbose_name="cnpj",
        null=True,
        unique=True
    )
    email = models.EmailField(
        verbose_name="email",
        max_length=256,
        null=True
    )
    phone = models.CharField(
        verbose_name="Whatsapp",
        max_length=11
    )
    is_whatsapp = models.BooleanField(
        verbose_name="se telefone é whatsapp",
        default=True
    )
    address_address = models.CharField(
        max_length=256,
        verbose_name="Logradouro"
    )
    address_zip_code = models.CharField(
        max_length=10,
        verbose_name="CEP"
    )
    address_number = models.CharField(
        max_length=256,
        verbose_name="Número"
    )
    address_district = models.CharField(
        max_length=256,
        verbose_name="Bairro"
    )
    address_city = models.CharField(
        max_length=256,
        verbose_name="Cidade"
    )
    address_city_ibge = models.CharField(
        max_length=10,
        verbose_name="IBGE cidade"
    )
    address_state = models.CharField(
        max_length=2,
        verbose_name="Estado"
    )
    
    
