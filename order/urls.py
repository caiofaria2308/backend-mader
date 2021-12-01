from django.urls import path
from .views import (
    NfeList,
    NfeViewSet,
    OrderList,
    OrderViewSet,
    OrderTypeStatusList,
    OrderMonthsList,
    OrderTypeDeliveryList,
    ProductList,
    ProductViewSet,
    SubwayStationList,
    SubwayStationViewSet,
    SubwayLineList,
    DeliveryMailList,
    DeliveryMailViewSet,
    DeliverySubwayList,
    DeliverySubwayViewSet
)

urlpatterns = [
    path('order/', OrderViewSet.as_view()),
    path('order/<str:pk>', OrderList.as_view()),
    path('order-month/', OrderMonthsList.as_view()),
    path('order-product/', ProductViewSet.as_view()),
    path('order-product/<str:pk>', ProductList.as_view()),
    path('order-type-status/', OrderTypeStatusList.as_view()),
    path('order-type-delivery/', OrderTypeDeliveryList.as_view()),
    path('subway-station/', SubwayStationViewSet.as_view()),
    path('subway-station/<str:pk>', SubwayStationList.as_view()),
    path('subway-line/', SubwayLineList.as_view()),
    path('delivery-mail/', DeliveryMailViewSet.as_view()),
    path('delivery-mail/<str:pk>', DeliveryMailList.as_view()),
    path('delivery-subway/', DeliverySubwayViewSet.as_view()),
    path('delivery-subway/<str:pk>', DeliverySubwayList.as_view()),
    path('nfe/', NfeViewSet.as_view()),
    path('nfe/<str:pk>', NfeList.as_view())
]
