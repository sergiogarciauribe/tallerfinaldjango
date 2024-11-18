from django.db import models

# Modelo CarritoCompra 

class CarritoCompra(models.Model): 

    porcentaje_descuento = models.FloatField(default=0) 

 

    def total_orden(self): 

        productos = self.lista_productos.all() 

        total = sum(p.precio for p in productos) 

        if self.porcentaje_descuento > 0: 

            total -= total * (self.porcentaje_descuento / 100) 

        return total 

 

    def agregar_producto(self, producto): 

        self.lista_productos.add(producto) 

 

    def remover_producto(self, id_producto): 

        self.lista_productos.filter(id=id_producto).delete() 