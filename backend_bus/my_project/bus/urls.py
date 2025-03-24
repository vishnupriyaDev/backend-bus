from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.bus_list, name='bus-list'),
    path('add/', views.add_bus, name='add-bus'),
    path('delete/<int:bus_id>/', views.delete_bus, name='delete-bus'),
]
