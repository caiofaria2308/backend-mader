from defaults import DefaultMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters

from .serializers import  (
    TypeSerializer,
    ProductSerializer
)

from .models import (
    Type,
    Product
)


class TypeViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Type.objects.all().order_by("name")
    serializer_class = TypeSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$name'
    ]
    
    
class TypeList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
    
class ProductViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$description',
        '$type_name'
    ]
    filterset_fields = [
        'type_name',
        'internal_code',
        'ean'
    ]
    
    
class ProductList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer = ProductSerializer