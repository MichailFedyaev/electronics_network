from django.apps import apps
from django.contrib import admin

app = apps.get_app_config("users")

for model in app.models.values():
    admin.site.register(model)
