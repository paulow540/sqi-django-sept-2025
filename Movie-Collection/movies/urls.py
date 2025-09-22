# movies/urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie-list'),
    path('movies/create/', views.movie_create, name='movie-create'),
    path('movies/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('movies/<int:pk>/edit/', views.movie_edit, name='movie-edit'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie-delete'),
]
