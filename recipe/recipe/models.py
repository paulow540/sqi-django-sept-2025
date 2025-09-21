from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200, help_text="Enter ingredients separated by commas") 
    instructions = models.CharField(max_length=250)
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    cover_image = models.ImageField(upload_to="cover_images/", blank=True, null=True, default="cover_images/default.jpg")


    def __str__(self):
        return f"{self.recipe_name} "
