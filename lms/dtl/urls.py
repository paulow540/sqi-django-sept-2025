from django.urls import path
from . import views

urlpatterns = [
    path("demo/", views.django_template_language, name="dtl_demo"),
    path("shopping_cart/", views.shopping_cart, name="shopping_cart"),
]