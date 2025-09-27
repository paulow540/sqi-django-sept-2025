from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class GenreChoices(models.TextChoices):
    ACTION = 'AC', 'Action'
    DRAMA = 'DR', 'Drama'
    COMEDY = 'CO', 'Comedy'
    HORROR = 'HO', 'Horror'
    ROMANCE = 'RO', 'Romance'
    SCIFI = 'SF', 'Science Fiction'
    FANTASY = 'FA', 'Fantasy'
    DOCUMENTARY = 'DO', 'Documentary'
    THRILLER = 'TH', 'Thriller'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=2, choices=GenreChoices.choices)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='movies',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date', 'title']

    def __str__(self):
        return f"{self.title} ({self.get_genre_display()})"

    def get_absolute_url(self):
        return reverse('movies:movie-detail', kwargs={'pk': self.pk})
