from django.db import models
from artists.models import Artist

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}  by {self.artist}"

