from django.urls import path 
from . import views 

app_name = "recipe"

urlpatterns = [
    path("home/", views.recipe_home_page, name="home"),
    path("list-all-recipe/", views.list_all_recipe, name="list-all-recipe"),
    path("recipe-description/<int:recipe_pk>", views.recipe_decription, name="recipe-description"),
    path("create-recipe/", views.create_recipe, name="create-recipe")
]

