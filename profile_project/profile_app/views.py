from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "profile_app/home.html")


def hobbies(request):
    return render(request, "profile_app/hobbies.html")


def goal(request):
    return render(request, "profile_app/goals.html")