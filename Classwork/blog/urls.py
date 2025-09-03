from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog_home, name="blog"),
    path("post/1/", views.blog_post, name="blog_post"),
    path("about/", views.blog_about, name="blog-about"),
]