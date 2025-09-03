from django.urls import path 
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("goal/", views.goal, name="goal"),
]

