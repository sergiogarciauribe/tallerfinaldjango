# api/urls.py 

from rest_framework.routers import DefaultRouter 

from .views import ClienteViewSet, AdministradorViewSet, ProductoViewSet, ProveedorViewSet, FacturaViewSet

 

router = DefaultRouter() 

router.register(r'clientes', ClienteViewSet) 

router.register(r'administradores', AdministradorViewSet) 

router.register(r'productos', ProductoViewSet) 

router.register(r'proveedores', ProveedorViewSet)

router.register(r'facturacion', FacturaViewSet)

urlpatterns = router.urls 