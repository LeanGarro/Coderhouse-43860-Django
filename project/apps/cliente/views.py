from django.shortcuts import render, redirect
from .models import Cliente, Pais


def home(request):
    clientes_registros = Cliente.objects.all()
    return render(request, "indec.html", {"clientes": clientes_registros})

def crear_clientes(request):
    from datetime import date
    
    p1 = Pais(nombre='peru')
    p2 = Pais(nombre="mexico")
    p3 = Pais(nombre="el salvador")
    
    p1.save()
    p2.save()
    p3.save()
    
    c1 = Cliente(nombre="almendra", apellido="ruiseñor", nacimiento= date(2015, 1, 1), pais_origen = p1)
    
    c1.save()
    return redirect("Cliente:home")