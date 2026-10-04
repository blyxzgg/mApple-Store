from django.urls import path
from .views import (
    shop_page, toggle_favorite, add_to_cart, favorites_page,
    cart_page, remove_from_cart, increase_quantity, decrease_quantity,
    remove_from_cart_by_product
)

app_name = 'shop'

urlpatterns = [
    path('', shop_page, name='home'),
    path('favorite/<int:product_id>/', toggle_favorite, name='toggle_favorite'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('favourites/', favorites_page, name='favorites'),

    path('cart/', cart_page, name='cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/remove_by_product/<int:product_id>/', remove_from_cart_by_product, name='remove_from_cart_by_product'),
]
