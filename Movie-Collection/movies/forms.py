from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Movie

User = get_user_model()

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

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='First name')
    last_name = forms.CharField(max_length=30, required=False, label='Last name')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")
