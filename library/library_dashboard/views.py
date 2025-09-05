from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def dashboard(request):
    context = {
        "librarian": "Kemi Adebayo",
        "books": [
            {
                "title": "Things Fall Apart",
                "author": "Chinua Achebe",
                "isbn": "978-0-385-47454-2",
                "category": "Literature",
                "available_copies": 3,
                "total_copies": 5,
                "publication_year": 1958,
                "is_featured": True,
                "price": 2500.00
            },
            {
                "title": "Purple Hibiscus",
                "author": "Chimamanda Ngozi Adichie",
                "isbn": "978-1-4000-7694-4",
                "category": "Literature",
                "available_copies": 0,
                "total_copies": 2,
                "publication_year": 2003,
                "is_featured": False,
                "price": 3200.00
            },
            {
                "title": "Half of a Yellow Sun",
                "author": "Chimamanda Ngozi Adichie",
                "isbn": "978-1-4000-4418-9",
                "category": "Historical Fiction",
                "available_copies": 1,
                "total_copies": 3,
                "publication_year": 2006,
                "is_featured": True,
                "price": 3800.00
            },
            {
                "title": "The Beautiful Ones Are Not Yet Born",
                "author": "Ayi Kwei Armah",
                "isbn": "978-0-435-90516-8",
                "category": "Literature",
                "available_copies": 2,
                "total_copies": 2,
                "publication_year": 1968,
                "is_featured": False,
                "price": 2800.00
            }
        ],
        "library_stats": {
            "total_members": 1247,
            "books_borrowed_today": 23,
            "overdue_books": 8,
            "new_arrivals_this_month": 15
        },
        "current_date": timezone.now(),
        "library_name": "Ibadan Central Library",
        "is_weekend": timezone.now().weekday() >= 5,
        "featured_message": "Discover African Literature Classics!"
    }

    return render(request, "dtl/dashboard.html", context)

