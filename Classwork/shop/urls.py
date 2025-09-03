from django.urls import path
from . import views


urlpatterns = [
    path("", views.shop, name="shop"),
    path("cart/", views.shop_cart, name="shop-cart"),
]