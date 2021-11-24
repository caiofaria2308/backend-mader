from django.urls import path
from .views import (
    ProductList,
    ProductViewSet,
    TypeCSOSNList,
    TypeCSTList,
    TypeList,
    TypeOriginList,
    TypeUnitViewSet,
    TypeViewSet
)

urlpatterns = [
    path('product/', ProductViewSet.as_view()),
    path('product/<str:pk>', ProductList.as_view()),
    
    path('type/', TypeViewSet.as_view()),
    path('type/<str:pk>', TypeList.as_view()),
    
    path('type-unit/', TypeUnitViewSet.as_view()),
    path('type-unit/<str:pk>', TypeUnitViewSet.as_view()),
    path('type-origin/', TypeOriginList.as_view()),
    path('type-origin/<str:pk>', TypeOriginList.as_view()),
    path('type-cst/', TypeCSTList.as_view()),
    path('type-cst/<str:pk>', TypeCSTList.as_view()),
    path('type-csosn/', TypeCSOSNList.as_view()),
    path('type-csosn/<str:pk>', TypeCSOSNList.as_view())
]
