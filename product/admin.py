from django.contrib import admin
from .models import Product, Ram, Storage, Color

admin.site.register(Product)
admin.site.register(Ram)
admin.site.register(Color)
admin.site.register(Storage)
