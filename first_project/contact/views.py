from django.shortcuts import render, HttpResponse

# Create your views here.



def phone_us(request):
    return HttpResponse("Phone us: '+234803062735'")


def email_us(request):
    return HttpResponse("Email us: 'opakunbpual@gmail.com'")