from django.contrib import admin
from .models import Product, Offer, Item


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Item, ItemAdmin)
