from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm

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


def album_detail(request, pk):
    all_album_details = get_object_or_404(Album, pk=pk)
    context = {
        "all_album_details": all_album_details
    }

    return render(request, "albums/album_detail.html", context)

def create_album(request):
    form = AlbumForm
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("albums:album-list")  

    context = {
        "form": form
    }

    return render(request, "albums/album_create.html", context)
