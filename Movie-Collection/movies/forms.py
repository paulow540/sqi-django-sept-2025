from django import forms
from .models import Movie, GenreChoices


class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_date', 'genre', 'description', 'poster']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }