from django.urls import path
from . import views

app_name = "albums"

urlpatterns = [
path("home-page", views.home_page, name="home-page"),
path("album-list", views.album_list, name="album-list"),
path("album-detail/<int:pk>/", views.album_detail, name="album-detail"),
]