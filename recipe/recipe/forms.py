from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields  = ["recipe_name","ingredients", "instructions", "cooking_time", "image", "cover_image"]