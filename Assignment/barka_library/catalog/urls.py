from django.urls import path
from . import views


urlpatterns = [
    path("", views.books_list, name="book_list"),
    path("special/", views.books_special, name="book_special"),
]
