from django.db import models
from datetime import datetime
import uuid


class Type(models.Model):
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
        verbose_name="se tipo de produto está ativo",
        default=True
    )
    name = models.CharField(
        verbose_name="nome do tipo de produto",
        unique=True,
        max_length=256
    )


class Product(models.Model):
    TYPE_UNIT = [
        ('UN', 'UNIDADE'),
        ('CX', 'CAIXA'),
        ('KG', 'KILOGRAMA'),
        ('PACOTE', 'PACOTE'),
        ('PC', 'PEÇA')
    ]
    TYPE_ORIGIN = [
        (0, 'Nacional, exceto as indicadas nos códigos 3 a 5 '),
        (1, 'Estrangeira - Importação direta, exceto a indicada no código 6 '),
        (2, 'Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 '),
        (3, 'Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40%'),
        (4, "Nacional, cuja produção tenha sido feita em conformidade com os processos "\
            "produtivos básicos de que tratam o Decreto-Lei nº 288/67 e as Leis nºs 8.248/91,"\
            "8.387/91, 10.176/01 e 11.484/07"
         ),
        (5, 'Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%'),
        (6 ,"Estrangeira - Importação direta, sem similar nacional, constante em lista de Resolução CAMEX"),
        (7, "Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista "\
            "de Resolução CAMEX"
        )
    ]
    TYPE_CST = [
        ('00', 'Tributada integralmente'),
        ('10', 'Tributada e com cobrança do ICMS por substituição tributária'),
        ('20', 'Com redução da BC'),
        ('30', 'Isenta / não tributada e com cobrança do ICMS por substituição tributária'),
        ('40', 'Isenta'),
        ('41', 'Não tributada'),
        ('50', 'Com suspensão'),
        ('51', 'Com diferimento'),
        ('60', 'ICMS cobrado anteriormente por substituição tributária'),
        ('70', 'Com redução da BC e cobrança do ICMS por substituição tributária'),
        ('90', 'Outras')
    ]
    TYPE_CSOSN = [
        (101, 'Tributada pelo Simples Nacional com permissão de crédito'),
        (102, 'Tributada pelo Simples Nacional sem permissão de crédito '),
        (103, 'Isenção do ICMS no Simples Nacional para faixa de receita bruta'),
        (201,"Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS "\
             "por substituição tributária"
        ),
        (202,"Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS "\
            "por substituição tributária"
        ),
        (203, "Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do "\
            "ICMS por substituição tributária "
        ),
        (300, 'Imune'),
        (400, 'Não tributada pelo Simples Nacional'),
        (500,"ICMS cobrado anteriormente por substituição tributária (substituído) ou por "\
            "antecipação "
        ),
        (900, 'Outros')
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
    is_active = models.BooleanField(
        verbose_name="se produto está ativo",
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
    cfop = models.SmallIntegerField(
        verbose_name="cfop",
        null=True
    )
    icms_modality = models.CharField(
        verbose_name="modalidade do icms",
        null=True,
        max_length=2,
        choices=TYPE_CST
    )
    icms_aliquot = models.DecimalField(
        verbose_name="aliquota icms",
        max_digits=10,
        decimal_places=2,
        null=True
    )
    icms_origin = models.SmallIntegerField(
        verbose_name="origem icms",
        null=True,
        choices=TYPE_ORIGIN
    )
    icms_csosn = models.SmallIntegerField(
        verbose_name="icms csosn",
        null=True,
        choices=TYPE_CSOSN
    )
    pis_modality = models.SmallIntegerField(
        verbose_name="modalidade pis",
        null=True
    )
    pis_aliquot = models.DecimalField(
        verbose_name="aliquota pis",
        max_digits=10,
        decimal_places=2,
        null=True
    )
    cofins_modality = models.SmallIntegerField(
        verbose_name="modalidade cofins",
        null=True
    )
    cofins_aliquot = models.DecimalField(
        verbose_name="aliquota cofins",
        max_digits=10,
        decimal_places=2,
        null=True
    )
    ipi_framework = models.SmallIntegerField(
        verbose_name="enquadramento ipi",
        null=True
    )
    ipi_aliquot = models.DecimalField(
        verbose_name="aliquota ipi",
        max_digits=10,
        decimal_places=2,
        null=True
    )
    
    
    @property
    def type_name(self):
        return self.type.name
    
    
    def save(self, *args, **kwargs):
        self.internal_code = int(datetime.utcnow().timestamp())
        super(Product, self).save(*args, **kwargs)