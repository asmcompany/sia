from VEGAN_API.VEGAN_API_CART.models import Cart, CartOrderDetail
from django.contrib import admin


class CartOrderDetailInline(admin.StackedInline):
    model = CartOrderDetail
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartOrderDetailInline,
        ]
