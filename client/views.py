from .models import Client
from .serializers import ClientSerializer

from defaults import DefaultMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters


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
    
    
class ClientList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
