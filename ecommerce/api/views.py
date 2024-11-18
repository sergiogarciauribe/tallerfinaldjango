from django.shortcuts import render
# Create your views here.

from rest_framework import viewsets 

from .models import Cliente, Administrador, Producto, CarritoCompra

from .serializers import ClienteSerializer, AdministradorSerializer, ProductoSerializer


from .models.proveedor import Proveedor
from .models.factura import Factura

from .serializers import ProveedorSerializer, FacturaSerializer
 

class ClienteViewSet(viewsets.ModelViewSet): 

    queryset = Cliente.objects.all() 

    serializer_class = ClienteSerializer 

 

class AdministradorViewSet(viewsets.ModelViewSet): 

    queryset = Administrador.objects.all() 

    serializer_class = AdministradorSerializer 

 

class ProductoViewSet(viewsets.ModelViewSet): 

    queryset = Producto.objects.all() 

    serializer_class = ProductoSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


