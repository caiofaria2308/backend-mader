from rest_framework import serializers
from .models import (
    Type,
    Product
)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        
        
class ProductSerializer(serializers.ModelSerializer):
    type_id = serializers.UUIDField()
    type_name = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"