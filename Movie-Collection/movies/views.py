from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import login
from .models import Movie
from .forms import MovieForm, SignUpForm

PAGINATE_BY = 12


def movie_list(request):
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
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


@login_required(login_url=reverse_lazy('movies:login'))
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect(movie.get_absolute_url())
    else:
        form = MovieForm()

    return render(request, 'movies/movie_form.html', {'form': form})


@login_required(login_url=reverse_lazy('movies:login'))
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # Only the user who added can edit
    if movie.added_by != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(movie.get_absolute_url())
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_form.html', {'form': form, 'movie': movie})


@login_required(login_url=reverse_lazy('movies:login'))
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    # Only the user who added can delete
    if movie.added_by != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        movie.delete()
        return redirect(reverse('movies:movie-list'))

    return render(request, 'movies/movie_confirm_delete.html', {'object': movie})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, populate first_name/last_name is already handled by form.save()
            messages.success(request, "Account created successfully. You are now logged in.")
            # Log the user in immediately
            login(request, user)
            return redirect('movies:movie-list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
