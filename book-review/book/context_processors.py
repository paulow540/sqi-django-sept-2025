from django.db.models import Avg
from book.models import Book

def top_rated_books(request):
    books = (
        Book.objects
        .annotate(avg_rating=Avg("review__rating"))
        .order_by("-avg_rating")[:2]
    )
    return {"sidebar_top_books": books}
