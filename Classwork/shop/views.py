from django.shortcuts import render, HttpResponse

# Create your views here.

def shop(request):
    return HttpResponse("Welcome to the Shop Home")

def shop_cart(request):
    return HttpResponse("Your shopping cart is empty")