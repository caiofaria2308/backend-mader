from django import http
from rest_framework.response import Response
from defaults import DefaultMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters, status

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
    queryset = Product.objects.all().order_by('description')
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$description'
    ]
    filterset_fields = [
        'internal_code',
        'ean'
    ]
    
    
class ProductList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('description')
    serializer = ProductSerializer
    
    
class TypeUnitViewSet(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Product.TYPE_UNIT)
            if kwargs:
                objs = {kwargs.get('pk'): objs.get(kwargs.get('pk'))}
            return Response(
                objs,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
    def post(self, request, *args, **kwargs):
        try:
            novo = (request.data["name"], request.data["value"])
            Product.TYPE_UNIT.append(novo)
            return Response(
                dict(Product.TYPE_UNIT),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class TypeOriginList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Product.TYPE_ORIGIN)
            if kwargs.get('pk'):
                objs = {kwargs.get('pk'): objs.get(kwargs.get('pk'))}
            return Response(
                objs, status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def post(self, request, *args, **kwargs):
        try:
            novo = (request.data["name"], request.data["value"])
            Product.TYPE_ORIGIN.append(novo)
            return Response(
                dict(Product.TYPE_ORIGIN),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class TypeCSTList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Product.TYPE_CST)
            if kwargs.get('pk'):
                objs = {kwargs.get('pk'): objs.get(kwargs.get('pk'))}
            return Response(
                objs, status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def post(self, request, *args, **kwargs):
        try:
            novo = (request.data["name"], request.data["value"])
            Product.TYPE_CST.append(novo)
            return Response(
                dict(Product.TYPE_CST),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class TypeCSOSNList(DefaultMixin, ListAPIView):
    def get(self, *args, **kwargs):
        try:
            objs = dict(Product.TYPE_CSOSN)
            if kwargs.get('pk'):
                objs = {kwargs.get('pk'): objs.get(kwargs.get('pk'))}
            return Response(
                objs, status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def post(self, request, *args, **kwargs):
        try:
            novo = (request.data["name"], request.data["value"])
            Product.TYPE_CSOSN.append(novo)
            return Response(
                dict(Product.TYPE_CSOSN),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
