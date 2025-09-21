from django import forms

from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "release_date", "artist", "album_image"]
        