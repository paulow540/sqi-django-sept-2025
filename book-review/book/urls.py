from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.list_all_books, name="list-all-books"),
    path("create-book/", views.create_book, name="create-book"),
    path("top-rated/", views.top_rated_books, name="top-rated"),
]