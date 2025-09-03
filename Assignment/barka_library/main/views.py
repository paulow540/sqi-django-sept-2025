from django.shortcuts import render, HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome to Barka Street Library</h1>")
