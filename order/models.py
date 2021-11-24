from django.db import models
from datetime import datetime
import uuid


class Order(models.Model):
    MONTHS = [
        (1, 'JANEIRO'),
        (2, 'FEVEREIRO'),
        (3, 'MARÇO'),
        (4, 'ABRIL'),
        (5, 'MAIO'),
        (6, 'JUNHO'),
        (7, 'JULHO'),
        (8, 'AGOSTO'),
        (9, 'SETEMBRO'),
        (10, 'OUTUBRO'),
        (11, 'NOVEMBRO'),
        (12, 'DEZEMBRO')
    ]
    TYPE_STATUS = [
        ('PENDENTE', 'Pendente'),
        ('PREPARANDO', 'Preparando'),
        ('ENTREGANDO', 'Em processo de entrega'),
        ('CONCLUIDO', 'Concluído')
    ]
    TYPE_DELIVERY = [
        ('N/A', "Sem entrega"),
        ('ESTACAO', 'Estação de metro/trem'),
        ('CORREIO', 'Correios')
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
    is_finished = models.BooleanField(
        verbose_name="se pedido foi finalizado",
        default=False
    )
    number = models.CharField(
        verbose_name="numéro do pedido",
        max_length=128,
        default="JAN0101010101",
        unique=True
    )
    store = models.ForeignKey(
        verbose_name="loja",
        to="store.Store",
        related_name="+",
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        to="client.Client",
        verbose_name="cliente",
        related_name="+",
        on_delete=models.CASCADE
    )
    delivery_date = models.DateTimeField(
        verbose_name="data de entrega",
        null=True
    )
    status = models.CharField(
        max_length=128,
        verbose_name="status do pedido",
        choices=TYPE_STATUS
    )
    type_delivery = models.CharField(
        max_length=128,
        verbose_name="tipo de entrega",
        choices=TYPE_DELIVERY
    )
    xml = models.TextField(
        verbose_name="xml",
        null=True
    )
    xml_key = models.TextField(
        verbose_name="chave do xml",
        null=True
    )
    additional_information = models.TextField(
        verbose_name="Informação adicional",
        null=True,
        blank=True
    )
    
    def save(self, *args, **kwargs):
        now = datetime.now()
        months = dict(self.MONTHS)
        month = months.get(now.month)[0:3]
        self.number = f"{month}{now.year}{now.month}{now.day}{now.hour}"\
                    f"{now.minute}{now.microsecond}"
        super(Order, self).save(*args, **kwargs)
    
    
class Product(models.Model):
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
    is_returned = models.BooleanField(
        verbose_name="se produto foi devolvido",
        default=False
    )
    order = models.ForeignKey(
        to="order.Order",
        verbose_name="pedido",
        related_name="+",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to="product.Product",
        verbose_name="produto",
        related_name="+",
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        verbose_name="quantidade"
    )
    discount = models.DecimalField(
        verbose_name="valor do desconto",
        max_digits=10,
        decimal_places=2
    )
    unit_value = models.DecimalField(
        verbose_name="valor unitário",
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    
    def save(self, *args, **kwargs):
        self.unit_value = self.product.sale_value
        super(Product, self).save(*args, **kwargs)
        
        
class SubwayStation(models.Model):
    LINES = [
        ('blue', "Linha 1 - Azul"),
        ('green', "Linha 2 - Verde"),
        ('red', 'Linha 3 - Vermelha'),
        ('yellow', 'Linha 4 - Amarela'),
        ('lilac', 'Linha 5 - Lilás'),
        ('ruby', 'Linha 7 - Ruby'),
        ('diamond', 'Linha 8 - Diamante'),
        ('emerald', 'Linha 9 - Esmeralda'),
        ('turquoise', 'Linha 10 - Turquesa'),
        ('coral', 'Linha 11 - Coral'),
        ('sapphire', 'Linha 12 - Safira'),
        ('jade', 'Linha 13 - Jade'),
        ('silver', 'Linha 15 - Prata')
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
        verbose_name="se estação está ativa",
        default=True
    )
    line = models.CharField(
        max_length=128,
        verbose_name="linha da estação",
        choices=LINES
    )
    name = models.CharField(
        max_length=128,
        verbose_name="nome da estação"
    )
    
             
class DeliverySubway(models.Model):
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
    is_delivered = models.BooleanField(
        verbose_name="se produto foi entregue",
        default=False
    )
    order = models.ForeignKey(
        to="order.Order",
        verbose_name="pedido",
        related_name="+",
        on_delete=models.CASCADE
    )
    delivered_date = models.DateTimeField(
        verbose_name="data de entrega"
    )
    station = models.ForeignKey(
        to="order.SubwayStation",
        related_name="+",
        verbose_name="estação",
        on_delete=models.CASCADE
    )
    responsible = models.ForeignKey(
        to="user.User",
        related_name="+",
        verbose_name="responsável",
        on_delete=models.CASCADE
    )
    
    
class DeliveryMail(models.Model):
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
    is_delivered = models.BooleanField(
        verbose_name="se produto foi entregue",
        default=False
    )
    order = models.ForeignKey(
        to="order.Order",
        verbose_name="pedido",
        related_name="+",
        on_delete=models.CASCADE
    )
    tracking_code = models.CharField(
        verbose_name="código de rastreio",
        max_length=128
    )
    
    
class Payment(models.Model):
    FORM_PAYMENT = [
        ('VISTA', 'À vista'),
        ('PRAZO', 'À prazo')
    ]
    TYPE_PAYMENT = [
        ('DINHEIRO', 'Dinheiro'),
        ('DEBITO', "Cartão de débito"),
        ('CRÉDITO', 'Cartão de crédito'),
        ('PIX', 'Pix')
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
    order = models.ForeignKey(
        to="order.Order",
        verbose_name="pedido",
        related_name="+",
        on_delete=models.CASCADE
    )
    is_paid = models.BooleanField(
        verbose_name="se produto foi pago",
        default=False
    )
    form_payment = models.CharField(
        verbose_name="forma de pagamento",
        max_length=128,
        choices=FORM_PAYMENT
    )
    type_payment = models.CharField(
        verbose_name="tipo de pagamento",
        max_length=128,
        choices=TYPE_PAYMENT
    )
    amount_paid = models.DecimalField(
        verbose_name="valor pago",
        max_digits=10,
        decimal_places=2
    )
    