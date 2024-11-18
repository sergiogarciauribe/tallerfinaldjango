# api/serializers.py 

from rest_framework import serializers
from .models import Cliente, Administrador, Producto, CarritoCompra, Proveedor, Factura
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

class CarritoCompraSerializer(serializers.ModelSerializer):
    lista_productos = ProductoSerializer(many=True)

    class Meta:
        model = CarritoCompra
        fields = ['lista_productos', 'porcentaje_descuento', 'total_orden']

class ClienteSerializer(serializers.ModelSerializer):
    carrito_compra = CarritoCompraSerializer()

    class Meta:
        model = Cliente
        fields = ['nombre', 'documento', 'direccion', 'correo', 'metodo_pago', 'id_cliente', 'carrito_compra']

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['nombre', 'documento', 'direccion', 'correo', 'metodo_pago', 'id_trabajador', 'fecha_vinculacion']


class FacturaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Factura

        fields = ['productos', 'precio_total', 'id_factura', 'iva', 'subtotal']

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor

        fields = ['nombre', 'documento', 'direccion', 'correo']
