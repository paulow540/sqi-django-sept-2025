from django.shortcuts import render

# Create your views here.

def stuent_info(request):
    return render(request, "student/student_info.html")
