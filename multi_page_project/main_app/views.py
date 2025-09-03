from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "main_app/home.html")


def about(request):
    return render(request, "main_app/about.html")

def contact(request):
    return render(request, "main_app/contact.html")