from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import User, Type
from .serializers import UserSerializer, TypeSerializer

from defaults import DefaultMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters, status
from mader.pagination import CustomPagination

# Create your views here.

class UserViewSet(DefaultMixin, ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$phone'
    ]
    pagination_class = CustomPagination
    
    
class UserList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    
    
    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj: User = get_object_or_404(
                    User,
                    pk=kwargs.get('pk')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.set_password(data["password"])
                obj.save()
                serializer = UserSerializer(obj)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
                
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TypeViewSet(DefaultMixin, ListCreateAPIView):
    queryset = Type.objects.all().order_by('name')
    serializer_class = TypeSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$name'
    ]
    pagination_class = CustomPagination
    
    
class TypeList(DefaultMixin, RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all().order_by('name')
    serializer_class = TypeSerializer
    pagination_class = CustomPagination
