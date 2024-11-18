from django.db import models

# Clase abstracta Usuario (usando abstract models de Django) 

class Usuario(models.Model): 

    nombre = models.CharField(max_length=100) 
    documento = models.CharField(max_length=20) 
    direccion = models.CharField(max_length=200) 
    correo = models.EmailField() 
    metodo_pago = models.CharField(max_length=50) 

    carrito_compra = models.OneToOneField('CarritoCompra', on_delete=models.CASCADE, null=True, blank=True) 

 

    class Meta: 

        abstract = True  # Esto indica que es una clase abstracta de Django 


    def mostrar_info(self) -> str: 

        raise NotImplementedError("Debe implementar el método mostrar_info") 