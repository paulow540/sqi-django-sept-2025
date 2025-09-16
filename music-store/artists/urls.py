from django.urls import path
from . import views

app_name = "artists"

urlpatterns = [
    path("artist-list", views.artist_list, name="artist-list"),
    path("artist-detail/<int:artist_pk>", views.artist_detail, name="artist-detail"),
]