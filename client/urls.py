from django.urls import path
from django.urls.conf import include
from .views import (
    ClientViewSet,
    ClientList
)

urlpatterns = [
    path('', ClientViewSet.as_view()),
    path('<str:pk>', ClientList.as_view()),
]