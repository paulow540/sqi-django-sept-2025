from django.urls import path
from . import views

urlpatterns = [
    path("", views.community, name="community"),
    path("events/", views.community_events, name = "community-events")
]