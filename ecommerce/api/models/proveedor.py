from django.db import models
from .Usuario import Usuario


class Proveedor (Usuario):
    Codigo_proveedor = models.CharField(max_length=50, unique=True)
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    nombre_representante = models.CharField(max_length=100)