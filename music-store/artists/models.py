from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    debut_year = models.IntegerField(max_length=4)


    def __str__(self):
        return f"{self.name} by {self.debut_year}"
