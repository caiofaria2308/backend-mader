from .views import (
    UserList,
    UserViewSet,
    TypeList,
    TypeViewSet
)
from django.urls import path

urlpatterns = [
    path('user/', UserViewSet.as_view()),
    path('user/<int:pk>', UserList.as_view()),
    
    path('type/', TypeViewSet.as_view()),
    path('type/<str:pk>', TypeList.as_view())
]
