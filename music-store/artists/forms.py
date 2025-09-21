from django import forms
from .models import Artist


class ArtistsForm(forms.ModelForm):
    class Meta:
        model = Artist

        fields = ["name","debut_year", "artist_image"]
