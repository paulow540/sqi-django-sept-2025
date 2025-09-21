from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def recipe_home_page(request):

    return render(request, "recipe/home_page.html")


def list_all_recipe(request):

    list_all_recipes = Recipe.objects.all()
    context = {
        "list_all_recipes": list_all_recipes
        }
    return render(request, "recipe/list_all_recipe.html", context)


def recipe_decription(request, recipe_pk):
    recipe_decription = get_object_or_404(Recipe, pk=recipe_pk)
    ingredients = recipe_decription.ingredients.split(",")
    context = {
        "recipe_decription":recipe_decription,
        "ingredients": ingredients
    }
    return render(request, "recipe/recipe_decription.html", context)



def create_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe:list-all-recipe')
    return render(request, "recipe/create_recipe.html", {'form': form})
