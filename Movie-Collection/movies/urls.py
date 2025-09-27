from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie-list'),
    path('movies/create/', views.movie_create, name='movie-create'),
    path('movies/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('movies/<int:pk>/edit/', views.movie_edit, name='movie-edit'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie-delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='movies:movie-list'), name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
]
