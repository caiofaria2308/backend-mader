from .models import Client
from .serializers import ClientSerializer

from defaults import DefaultMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from mader.pagination import CustomPagination


class ClientViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$name',
        '$phone'
    ]
    filterset_fields = [
        'document_number',
        'document_type'
    ]
    pagination_class = CustomPagination
    
    
class ClientList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = CustomPagination
