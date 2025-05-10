from django.core.management import call_command
from django.core.management.base import BaseCommand

from suppliers.models import Supplier, Product


class Command(BaseCommand):
    help = "Загрузка тестовых данных из фикстур"

    def handle(self, *args, **kwargs):
        # Удаление всех поставщиков и продуктов
        self.stdout.write("Удаление старых записей...")
        Supplier.objects.all().delete()
        Product.objects.all().delete()

        # Загрузка фикстур
        self.stdout.write("Загрузка поставщиков...")
        call_command("loaddata", "example_suppliers.json", format="json")
        self.stdout.write(self.style.SUCCESS("Поставщики загружены успешно."))

        self.stdout.write("Загрузка продуктов и связей...")
        call_command("loaddata", "example_products.json", format="json")
        self.stdout.write(self.style.SUCCESS("Продукты и связи загружены успешно."))
