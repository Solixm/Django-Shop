from django.contrib import admin
from .models import Product, Ram, Storage, Color
from . import models


class InformationAdmin(admin.StackedInline):
    model = models.Information


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'des', 'price')
    inlines = (InformationAdmin,)


admin.site.register(Ram)
admin.site.register(Color)
admin.site.register(Storage)
