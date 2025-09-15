from django.shortcuts import render
from .models import Album

# Create your views here.

def home_page(request):
    return render(request, "albums\home_page.html")


def album_list(request):
    all_album_lists = Album.objects.all().order_by("-release_date")  
    # artists_name = all_album_lists.get()
    context = {
        "all_album_lists": all_album_lists

    }
    return render(request, "albums/album_list.html", context)
