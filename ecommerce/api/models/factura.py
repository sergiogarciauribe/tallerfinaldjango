from django.db import models
from .producto import Producto


class Factura (Producto):
    productos = models.ManyToManyField(Producto,related_name="facturas" )
    precio_total = models.FloatField()
    id_factura = models.CharField(max_length=50)
    iva = models.FloatField()
    subtotal = models.FloatField()





