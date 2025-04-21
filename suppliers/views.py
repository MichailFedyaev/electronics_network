from rest_framework import viewsets, filters
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsActiveStaff


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveStaff]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['country', 'city', 'name']
    ordering_fields = ['name', 'created_at', 'debt']
