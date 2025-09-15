from django.urls import path
from . import views

app = "student"

urlpatterns = [
    path("student-info",views.stuent_info, name="student-info"),
]
