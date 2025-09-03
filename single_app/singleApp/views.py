from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "singleApp/home.html")

def profile(request):
    return render(request,  "singleApp/profile.html")

def services(request):
    return render(request, "singleApp/services.html")

def help(request):
    return render(request, "singleApp/help.html")