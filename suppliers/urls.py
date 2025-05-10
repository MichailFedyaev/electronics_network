from suppliers.apps import SuppliersConfig
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet


app_name = SuppliersConfig.name

router = DefaultRouter()
router.register(r'', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', include(router.urls)),
]
