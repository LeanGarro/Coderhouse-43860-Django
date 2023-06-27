from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
	return HttpResponse("<h1>Segunda vista</h1>")

def nombre(request, nombre: str, apellido: str):
	nombre =  nombre.capitalize()
	apellido = apellido.capitalize()
	return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
	mi_html = open("./templates/template1.html")
	#mi_template = Template(mi_html.read())
	mi_html.close()
	nombre = "Luis" #! nuevo
	apellido = "Van Beethoven" #! nuevo
	datos = {"nombre": nombre, "apellido": apellido,} #! nuevo
	datos["fecha"]: ahora
	#mi_contexto = Context(datos) #! cambios
	#mi_documento = mi_template.render(mi_contexto)
	return render(request, "template1.html", context=datos)

def ahora(request):
	ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f")
	return HttpResponse(f"<h1> Feche y Hora: {ahora} </h1>")

def mis_notas(request):
	lista = [2, 3, 4, 5, 7, 8, 9, 10]
	contexto = {"notas": lista}
	return render(request, "notas.html", contexto)

def amigos(request):
	amigos = ["juan", "nahuel", "sarmiento", "jose"]
	contexto = {"amigos": amigos}
	return render(request, "nuevo.html", contexto)
