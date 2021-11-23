from django.urls import path
from .views import StoreViewSet, StoreList

urlpatterns = [
    path('', StoreViewSet.as_view()),
    path('<str:pk>', StoreList.as_view()),
]