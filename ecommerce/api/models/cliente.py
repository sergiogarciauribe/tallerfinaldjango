from django.db import models

from.Usuario import Usuario

# Clase Cliente que hereda de Usuario 

class Cliente(Usuario): 

    id_cliente = models.CharField(max_length=50) 

 

    def mostrar_info(self) -> str: 

        return f"Cliente: {self.nombre}, ID Cliente: {self.id_cliente}" 

 

    def pagar(self, metodo_pago: str) -> bool: 

        print(f"Cliente {self.nombre} ha pagado con {metodo_pago}.") 

        return True 