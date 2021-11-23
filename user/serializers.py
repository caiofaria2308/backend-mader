from rest_framework import serializers

from store.serializers import StoreSerializer
from .models import User, Type
from store.models import Store


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Type
        
        
class UserSerializer(serializers.ModelSerializer):
    type_id = serializers.UUIDField()
    type = TypeSerializer(read_only=True)
    store_id = serializers.UUIDField()
    store = StoreSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = "__all__"
        
