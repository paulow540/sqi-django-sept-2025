# movies/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .models import Movie
from .forms import MovieForm

PAGINATE_BY = 12


def movie_list(request):
    """List all movies with pagination."""
    qs = Movie.objects.all().order_by('-release_date', 'title')
    paginator = Paginator(qs, PAGINATE_BY)
    page = request.GET.get('page', 1)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    context = {
        'movies': movies,
        'is_paginated': movies.has_other_pages(),
        'page_obj': movies,
        'paginator': paginator,
    }
    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, pk):
    """Show details for a single movie."""
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def movie_create(request):
    """Create a new movie (handles file upload)."""
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect(movie.get_absolute_url())
    else:
        form = MovieForm()

    return render(request, 'movies/movie_form.html', {'form': form})


def movie_edit(request, pk):
    """Edit an existing movie."""
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(movie.get_absolute_url())
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_form.html', {'form': form, 'movie': movie})


def movie_delete(request, pk):
    """
    Confirm-and-delete view.
    GET -> show confirmation template
    POST -> delete and redirect to list
    """
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        # If you want to also delete the poster file from disk, you can do it here:
        # if movie.poster and movie.poster.path:
        #     try:
        #         os.remove(movie.poster.path)
        #     except Exception:
        #         pass
        movie.delete()
        return redirect(reverse('movies:movie-list'))

    return render(request, 'movies/movie_confirm_delete.html', {'object': movie})
