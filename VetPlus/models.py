from django.db import models
from django import forms

# Create your models here.

class InicioSesion(models.Model):
    usuario = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=20)


class Busqueda_Cliente(models.Model):
    cliente = models.CharField(max_length=20)
    rut= models.IntegerField()


    
