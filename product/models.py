from django.db import models
import uuid


class Type(models.Model):
    id = models.UUIDField(
        verbose_name="id",
        primary_key=True,
        default=uuid.uuid5(uuid.uuid4(),"mader_client")
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
        verbose_name="se tipo de produto está ativo",
        default=True
    )
    name = models.CharField(
        verbose_name="nome do tipo de produto",
        unique=True,
        max_length=256
    )


class Product(models.Model):
    TYPE_UNIT = (
        ('UN', 'UNIDADE'),
        ('CX', 'CAIXA'),
        ('KG', 'KILOGRAMA'),
        ('PACOTE', 'PACOTE'),
        ('PC', 'PEÇA')
    )
    id = models.UUIDField(
        verbose_name="id",
        primary_key=True,
        default=uuid.uuid5(uuid.uuid4(),"mader_client")
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
        verbose_name="se tipo de produto está ativo",
        default=True
    )
    type = models.ForeignKey(
        to="product.Type",
        related_name="+",
        verbose_name="tipo do produto",
        on_delete=models.CASCADE
    )
    internal_code = models.BigIntegerField(
        verbose_name="código interno",
        default=1
    )
    description = models.CharField(
        verbose_name="nome do produto",
        max_length=256
    )
    comercial_unit = models.CharField(
        verbose_name="unidade de medida",
        max_length=10,
        choices=TYPE_UNIT
    )
    taxable_unit = models.CharField(
        verbose_name="unidade de medida tributável",
        max_length=10,
        choices=TYPE_UNIT
    )
    ean = models.CharField(
        verbose_name="Código de barras",
        max_length=128,
        default="SEM GTIN"
    )
    taxable_ean = models.CharField(
        verbose_name="Código de barras",
        max_length=128,
        default="SEM GTIN"
    )
    sale_value = models.DecimalField(
        verbose_name="valor de venda",
        decimal_places=2,
        max_digits=10
    )
    ncm = models.CharField(
        verbose_name="ncm",
        max_length=20,
        null=True
    )
    cest = models.CharField(
        verbose_name="cest",
        max_length=20,
        null=True
    )
    cfop = models.CharField(
        verbose_name="cfop",
        max_length=4,
        null=True
    )
    icms_modality = models.CharField(
        verbose_name="modalidade do icms",
        max_length=5,
        null=True
    )
    icms_aliquot = models.CharField(
        verbose_name="aliquota icms",
        max_length=10,
        null=True
    )
    icms_origin = models.CharField(
        verbose_name="origem icms",
        max_length=10,
        null=True
    )
    icms_csosn = models.CharField(
        verbose_name="icms csosn",
        max_length=10,
        null=True
    )
    pis_modality = models.CharField(
        verbose_name="modalidade pis",
        max_length=10,
        null=True
    )
    pis_aliquot = models.CharField(
        verbose_name="aliquota pis",
        max_length=10,
        null=True
    )
    cofins_modality = models.CharField(
        verbose_name="modalidade cofins",
        max_length=10,
        null=True
    )
    cofins_aliquot = models.CharField(
        verbose_name="aliquota cofins",
        max_length=10,
        null=True
    )
    ipi_framework = models.CharField(
        verbose_name="enquadramento ipi",
        max_length=10,
        null=True
    )
    ipi_aliquot = models.CharField(
        verbose_name="aliquota ipi",
        max_length=10,
        null=True
    )
    
    
    @property
    def type_name(self):
        return self.type.name
    
    
    def save(self, *args, **kwargs):
        if self.__state.adding:
            last_id = self.objects.all().aggregate(largest=models.Max('internal_code'))
            if last_id is not None:
                self.internal_code = last_id + 1
        super(Product, self).save(*args, **kwargs)