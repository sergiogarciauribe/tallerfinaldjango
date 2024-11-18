from email.contentmanager import raw_data_manager

from django.core.management.base import BaseCommand
from api.models.proveedor import Proveedor
from api.models.factura import Factura
from api.models.producto import Producto



from faker import Faker

import random


class Command(BaseCommand):
    help = 'Populate the database with fake proveedores and facturas'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            proveedor = Proveedor.objects.create(
                nombre=fake.first_name(),
                documento=fake.bothify(text='DOC###'),
                direccion=fake.address(),
                correo=fake.email()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake proveedor'))


        productos = list(Producto.objects.all())
        if not productos:
            self.stdout.write(self.style.ERROR('No hay productos en la base de datos.'))
            return  # Salir si no hay productos
        for _ in range(10):
            factura = Factura.objects.create(
                precio_total=random.uniform(100,1000),
                id_factura=fake.unique.bothify(text='FAC###'),
                iva=19.0,
                subtotal=random.uniform(80,950)
            )
            factura.productos.set(random.sample(productos, k=random.randint(1, len (productos))))
        self.stdout.write(self.style.SUCCESS('Successfully facturas faker databases'))





