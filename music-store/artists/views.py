from django.shortcuts import render
from .models import Artist

# Create your views here.

def artist_list(request):
    all_artist_lists = Artist.objects.all().order_by("-debut_year")  



    context = {
        "all_artist_lists": all_artist_lists

    }
    return render(request, "artists/artist_list.html", context)
