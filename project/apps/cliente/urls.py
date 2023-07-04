from django.contrib import admin
from django.urls import path, include
from .views import home, crear_clientes



urlpatterns = [
    path("", home, name= "home"),
    path("crear_clientes/", crear_clientes, name= "crear_clientes"),
]
