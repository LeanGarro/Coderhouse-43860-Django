from django.shortcuts import render
from .models import Cliente


def home(request):
    clientes_registros = Cliente.objects.all()
    return render(request, "indec.html", {"app": "aplicacion producto"})