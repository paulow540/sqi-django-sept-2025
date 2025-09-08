from django.urls import path 
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("services/", views.services_view, name="services"),
    path("testimonials", views.testimonials_view, name="testimonials"),
    path("pricing", views.pricing_view, name="pricing"),
]