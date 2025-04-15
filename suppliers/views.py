from rest_framework import viewsets, filters
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsActiveStaff


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']  # фильтрация по стране