from .models import Store
from .serializers import StoreSerializer

from defaults import DefaultMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters


class StoreViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Store.objects.all().order_by('fantasy_name')
    serializer_class = StoreSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$company_name',
        '$fantasy_name'
    ]
    filterset_fields = [
        'cnpj'
    ]
    
    
class StoreList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all().order_by('fantasy_name')
    serializer_class = StoreSerializer
