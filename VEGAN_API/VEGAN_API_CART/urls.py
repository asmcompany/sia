from VEGAN_API.VEGAN_API_CART.views import add_to_cart, proceed_to_checkout, remove_from_cart
from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart_page'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart_page'),
    path('proceed/', proceed_to_checkout, name='proceed_to_checkout_page'),
]
