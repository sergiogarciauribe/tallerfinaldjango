from itertools import product

from django.core.management.base import BaseCommand
from api.models import Producto

from faker import Faker

import random


class Command(BaseCommand):
    help = 'Populate the database with fake products, proveedores and facturas'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Genera 20 productos falsos

        for _ in range(20):
            nombre = fake.word().capitalize()

            precio = round(random.uniform(10.0, 100.0), 2)  # Precios aleatorios entre 10 y 100

            Producto.objects.create(nombre=nombre, precio=precio)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake products'))