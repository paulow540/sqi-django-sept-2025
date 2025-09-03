from django.shortcuts import render, HttpResponse

# Create your views here.

def blog_home(request):
    return HttpResponse("Welcome to the Blog Home")



def blog_post(request):
    return HttpResponse("This is blog post #1")

def blog_about(request):
    return  HttpResponse("About the Blog")