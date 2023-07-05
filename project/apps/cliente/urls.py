from django.contrib import admin
from django.urls import path, include
from .views import home, crear_clientes, crear_cliente



urlpatterns = [
    path("", home, name= "home"),
    path("crear_clientes/", crear_clientes, name= "crear_clientes"),
    path("cliente/", include("cliente.urls")),
    path("producto", include("producto.urls")),
    path('crear/', crear_cliente, name= "crear"),
]
