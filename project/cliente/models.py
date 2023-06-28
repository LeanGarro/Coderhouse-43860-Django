from django.db import models

class pais(models.Model):
    nombre= models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nombre

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_de_origen = models.ForeignKey(pais, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
