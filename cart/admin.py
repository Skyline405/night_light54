from django.contrib import admin

from cart.models import Cart, Item


# DEBUG ONLY

# class ItemInline(admin.TabularInline):
#     model = Item
#
#
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     inlines = [ItemInline]
