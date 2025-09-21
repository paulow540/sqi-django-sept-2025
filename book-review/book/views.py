from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.db.models import Avg

# Create your views here.

def list_all_books(request):
    book = Book.objects.all()
    context = {
        "all_books": book
    }
    return render(request, "book/list_all_book.html", context)


def create_book(request):
    form = BookForm
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()       
            return redirect('book:list-all-books')

    context = {
        'form': form
    }

    return render(request, "book/create_book.html", context)


def top_rated_books(request):
    # Annotate each book with its average rating
    books = (
        Book.objects
        .annotate(avg_rating=Avg("review__rating"))  # "review" is the related_name from Review → Book FK
        .order_by("-avg_rating")[:2]  # Top 2
    )

    context = {"books": books}
    return render(request, "book/top_rated_books.html", context)