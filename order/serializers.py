from django.db.models import fields
from rest_framework import serializers

from user.serializers import UserSerializer
from .models import (
    Order,
    Product,
    SubwayStation,
    DeliverySubway,
    DeliveryMail,
    Payment
)
from store.serializers import StoreSerializer
from client.serializers import ClientSerializer
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    store_id = serializers.UUIDField()
    client = ClientSerializer(read_only=True)
    client_id = serializers.UUIDField()
    
    class Meta:
        model = Order
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.UUIDField()
    product = ProductSerializer(read_only=True)
    product_id = serializers.UUIDField()
    
    class Meta:
        model = Product
        fields = "__all__"
        
        
class SubwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStation
        fields = "__all__"
        
        
class DeliverySubwaySerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.UUIDField()
    responsible = UserSerializer(read_only=True)
    responsible_id = serializers.IntegerField()
    station = SubwaySerializer(read_only=True)
    station_id = serializers.UUIDField()
    
    class Meta:
        model = DeliverySubway
        fields = "__all__"
        

class DeliveryMailSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.UUIDField()
    
    class Meta:
        model = DeliveryMail
        fields = "__all__"
    
    
class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.UUIDField()
    
    class Meta:
        model = Payment
        fields = "__all__"