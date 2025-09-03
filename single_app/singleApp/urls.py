from django.urls import path
from . import views

urlpatterns  = [
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("services/", views.services, name="services"),
    path("help/", views.help, name="help"),
]