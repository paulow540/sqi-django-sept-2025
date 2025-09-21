from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from book.models import Book
from .forms import ReviewForm

# Create your views here.




def book_review_details(request, book_pk):
    book_obj = get_object_or_404(Book, pk=book_pk)
    # only reviews belonging to this book
    print(book_obj)
    reviews = book_obj.review_set.all().order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # create but don't save yet, attach book, then save
            review = form.save(commit=False)
            review.book = book_obj
            review.save()
            return redirect('review:book-review-details', book_pk=book_pk)
    else:
        form = ReviewForm()

    context = {
        "book_review_details": book_obj,
        "reviews": reviews,
        "form": form,
    }
    return render(request, "review/book_review_details.html", context)
