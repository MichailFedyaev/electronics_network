from django.contrib import admin
from .models import Supplier, Product
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'country',
        'city',
        'street',
        'house_number',
        'debt',
        'created_at',
        'supplier_link',
        'level',
    )
    list_filter = ('city',)
    search_fields = ('name', 'city', 'country', 'email')
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:suppliers_supplier_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return '-'
    supplier_link.short_description = "Поставщик"

    def level(self, obj):
        return obj.get_level()
    level.short_description = "Уровень"

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        updated = queryset.update(debt=0)
        self.message_user(request, f"У {updated} звеньев сети задолженность была обнулена.")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
