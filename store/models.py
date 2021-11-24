from django.db import models
from django_cpf_cnpj.fields import CNPJField
import uuid

# Create your models here.
class Store(models.Model):
    REGIMES = [
        ("1", "SIMPLES NACIONAL"),
        ("3", "NORMAL")
    ]
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
    company_name = models.CharField(
        verbose_name="razão social",
        max_length=256
    )
    fantasy_name = models.CharField(
        verbose_name="nome fantasia",
        max_length=256
    )
    phone = models.CharField(
        verbose_name="Whatsapp",
        max_length=11
    )
    is_whatsapp = models.BooleanField(
        verbose_name="se telefone é whatsapp",
        default=True
    )
    cnpj = CNPJField(unique=True)
    tax_regime = models.CharField(
        verbose_name="regime tributário",
        max_length=1,
        choices=REGIMES
    )
    state_registration = models.CharField(
        max_length=20,
        verbose_name="Inscrição estadual",
        null=True,
        blank=True
    )
    municipal_registration = models.CharField(
        max_length=20,
        verbose_name="Inscrição municipal",
        null=True,
        blank=True
    )
    cnae = models.CharField(
        max_length=20,
        verbose_name="CNAE Fiscal",
        null=True,
        blank=True
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
    nfe_certified = models.TextField(
        verbose_name="Certificado digital",
        null=True,
        blank=True
    )
    nfe_password = models.CharField(
        verbose_name="Senha do certificado digital",
        max_length=256,
        null=True,
        blank=True
    )
    nfe_homologation = models.BooleanField(
        verbose_name="nfe em modo de homologação",
        default=True
    )
    