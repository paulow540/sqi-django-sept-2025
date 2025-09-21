from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('book-review-details/<int:book_pk>/', views.book_review_details, name='book-review-details'),
]
