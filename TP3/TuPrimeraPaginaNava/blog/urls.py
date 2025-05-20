from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cliente/', views.agregar_cliente, name="agregar_cliente"),
    path('servicio/', views.agregar_servicio, name="agregar_servicio"),
    path('contratacion/', views.agregar_contratacion, name="agregar_contratacion"),
    path('buscar-cliente/', views.buscar_cliente, name="buscar_cliente"),
]