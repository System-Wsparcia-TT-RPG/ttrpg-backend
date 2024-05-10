import importlib
import inspect

from django.contrib import admin

# Registers all models from the models.py file in the web.api app
for _, cls in inspect.getmembers(importlib.import_module('.models', 'web.api'), inspect.isclass):
    if cls.__module__ == 'web.api.models':
        admin.site.register(cls)
