from django.shortcuts import render, get_object_or_404
from .models import Artist

# Create your views here.

def artist_list(request):
    all_artist_lists = Artist.objects.all().order_by("-debut_year")  
    context = {
        "all_artist_lists": all_artist_lists
    }
    return render(request, "artists/artist_list.html", context)

def artist_detail(request, artist_pk):
    all_artist_details = get_object_or_404(Artist, pk=artist_pk)
    context = {
        "all_artist_details": all_artist_details
    }
    return render(request, "artists/artist_detail.html",context )



