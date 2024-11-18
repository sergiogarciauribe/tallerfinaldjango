from django.db import models
# Modelo Producto 

class Producto(models.Model): 

    nombre = models.CharField(max_length=100) 

    precio = models.FloatField(null=True, blank=True)

 



 