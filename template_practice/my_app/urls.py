from django.urls import path
from . import views


urlpatterns = [
    path("my_app/", views.welcome, name="my-app" ),
]