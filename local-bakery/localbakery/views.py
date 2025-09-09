from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "title": "Welcome to Sweet Crust Bakery",
        "tagline": "Freshly baked goodness, every day!",
        "specials": [
            {"name": "Sourdough Bread", "price": "$4"},
            {"name": "Chocolate Croissant", "price": "$2.5"},
            {"name": "Blueberry Muffin", "price": "$2"},
        ],
    }
    return render(request, "bakery/home.html", context)


def menu(request):
    menu_items = [
        {
            "category": "Breads",
            "items": [
                {"name": "Sourdough", "image": "images/Sourdough.jpg", "price": "$4"},
                {"name": "Baguette", "image": "images/Baguette.jpg", "price": "$2.8"},
                {"name": "Whole Wheat", "image": "images/Whole Wheat.jpg", "price": "$4.7"},
            ],
        },
        {
            "category": "Pastries",
            "items": [
                {"name": "Croissant", "image": "images/Croissant.jpg", "price": "$6"},
                {"name": "Danish", "image": "images/Danish.jpg", "price": "$3.6"},
                {"name": "Muffin", "image": "images/Muffin.jpg", "price": "$5.6"},

            ],
        },
        {
            "category": "Cakes",
            "items": [
                {"name": "Chocolate Cake", "image": "images/Chocolate Cake.jpg", "price": "$5.7"},
                {"name": "Cheesecake", "image": "images/Cheesecake.jpg", "price": "$7.9"},
                {"name": "Carrot Cake", "image": "images/Carrot Cake.jpg", "price": "$7.6"},

            ],
        },
    ]

    return render(request, "bakery/menu.html", context={"menu_items": menu_items})



def contact(request):
    context = {
        "title": "Contact Us",
        "address": "123 Baker Street, Springfield",
        "phone": "+234 801 234 5678",
        "email": "info@sweetcrustbakery.com",
        "opening_hours": {
            "Mon-Fri": "7:00 AM - 7:00 PM",
            "Sat-Sun": "8:00 AM - 5:00 PM",
        },
    }
    return render(request, "bakery/contact.html", context)


def about(request):
    context = {
        "title": "About Sweet Crust Bakery",
        "story": "Sweet Crust Bakery has been serving freshly baked bread, cakes, and pastries since 2005. Our mission is to bring smiles through every bite!",
        "values": ["Fresh Ingredients", "Homemade Taste", "Community First"],
        "teams": [
            {"name": "Jane Doe", "role": "Head Baker"},
            {"name": "John Smith", "role": "Pastry Chef"},
        ],
    }
    return render(request, "bakery/about.html", context)
