from rest_framework.response import Response
from defaults import DefaultMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters, status


from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.utils.flags import CODIGO_BRASIL

from mader.pagination import CustomPagination


from .serializers import (
    NfeSerializer,
    OrderSerializer,
    ProductSerializer,
    SubwaySerializer,
    DeliveryMailSerializer,
    DeliverySubwaySerializer,
    PaymentSerializer
)

from .models import (
    Nfe,
    Order,
    Product,
    SubwayStation,
    DeliverySubway,
    DeliveryMail,
    Payment
)


class OrderViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Order.objects.all().order_by("created_at").reverse()
    serializer_class = OrderSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$number'
    ]
    filterset_fields = [
        'status',
        'client',
        'is_finished',
        'type_delivery'
    ]
    pagination_class = CustomPagination
    

class OrderList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    
    
class OrderMonthsList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Order.MONTHS)
            if kwargs.get('pk'):
                objs = objs.get(kwargs.get('pk'))
            return Response(objs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class OrderTypeStatusList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Order.TYPE_STATUS)
            if kwargs.get('pk'):
                objs = objs.get(kwargs.get('pk'))
            return Response(objs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class OrderTypeDeliveryList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Order.TYPE_DELIVERY)
            if kwargs.get('pk'):
                objs = objs.get(kwargs.get('pk'))
            return Response(objs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    
class ProductViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Product.objects.all().order_by("created_at").reverse()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'order',
        'product'
    ]
    pagination_class = CustomPagination
    
    
class ProductList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    
    
class SubwayStationViewSet(DefaultMixin, ListCreateAPIView):
    queryset = SubwayStation.objects.all().order_by('name')
    serializer_class = SubwaySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'line'
    ]
    search_fields = [
        '$name'
    ]
    pagination_class = CustomPagination
    
    
class SubwayStationList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = SubwayStation.objects.all()
    serializer_class = SubwaySerializer
    pagination_class = CustomPagination
    

class SubwayLineList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(SubwayStation.LINES)
            if kwargs.get('pk'):
                objs = objs.get(kwargs.get('pk'))
            return Response(objs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    

class DeliverySubwayViewSet(DefaultMixin, ListCreateAPIView):
    queryset = DeliverySubway.objects.all().order_by('delivered_date').reverse()
    serializer_class = DeliverySubwaySerializer
    filterset_fields = [
        'order',
        'station',
        'responsible',
        'delivered_date'
    ]
    pagination_class = CustomPagination
    
    
class DeliverySubwayList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = DeliverySubway.objects.all()
    serializer_class = DeliverySubwaySerializer
    pagination_class = CustomPagination
    
        
class DeliveryMailViewSet(DefaultMixin, ListCreateAPIView):
    queryset = DeliveryMail.objects.all().order_by('created_at').reverse()
    serializer_class = DeliveryMailSerializer
    filterset_fields = [
        'order',
        'tracking_code'
    ]
    pagination_class = CustomPagination
    
    
class DeliveryMailList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = DeliveryMail.objects.all()
    serializer_class = DeliveryMailSerializer
    pagination_class = CustomPagination
    
    
class PaymentViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Payment.objects.all().order_by('created_at').reverse()
    serializer_class = PaymentSerializer
    filterset_fields = [
        'order',
        'is_paid'
    ]
    pagination_class = CustomPagination
    
    
class PaymentList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = CustomPagination
    
    
class FormPaymentList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Payment.FORM_PAYMENT)
            if kwargs.get('pk'):
                objs = objs.get(kwargs.get('pk'))
            return Response(objs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    
class TypePaymentList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Payment.TYPE_PAYMENT)
            if kwargs.get('pk'):
                objs = objs.get(kwargs.get('pk'))
            return Response(objs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
                  
class NfeViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Nfe.objects.all().order_by('created_at').reverse()
    serializer_class = NfeSerializer
    filterset_fields = [
        'order'
    ]
    pagination_class = CustomPagination
    
    
class NfeList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Nfe.objects.all()
    serializer_class = NfeSerializer
    pagination_class = CustomPagination