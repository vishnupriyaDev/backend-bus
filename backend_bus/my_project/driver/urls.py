from django.urls import path
from . import views

urlpatterns = [
    path('bus/list/', views.bus_list, name='bus-list'),
    path('bus/delete/<int:pk>/', views.bus_delete, name='bus-delete'),
    path('driver/list/', views.driver_list, name='driver-list'),
    path('driver/delete/<int:pk>/', views.driver_delete, name='driver-delete'),
    path('driver/add/', views.driver_add, name='driver-add'),  
]
