from django.db import models
from.Usuario import Usuario
# Clase Administrador que hereda de Usuario 

class Administrador(Usuario): 

    id_trabajador = models.CharField(max_length=50) 

    fecha_vinculacion = models.DateField() 

 

    def mostrar_info(self) -> str: 

        return f"Administrador: {self.nombre}, ID Trabajador: {self.id_trabajador}" 

 

    def pagar(self, metodo_pago: str) -> bool: 

        print(f"Administrador {self.nombre} ha aprobado un pago con {metodo_pago}.") 

        return True 

 

 

 