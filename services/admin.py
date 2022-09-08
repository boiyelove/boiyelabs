from django.contrib import admin
from .models import Catalog, Service, Tag, Portfolio

items = (Catalog, Service, Tag, Portfolio)
for item in items:
	admin.site.register(item)

# Register your models here.
