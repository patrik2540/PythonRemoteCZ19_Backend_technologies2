from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from viewer.models import *


def hello(request):
    return HttpResponse("Hello World")


def hello2(request, s):
    return HttpResponse(f'Hello, {s} word!')


def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} word!')


def hello4(request):
    adjective = ['nice', 'beutiful', 'cruel', 'blue', 'green']
    context = {'adjectives': adjective, 'name': 'Patrik'}
    return render(
        request=request,
        template_name="hello.html",
        context=context
    )


def home(request):
    return render(request, "home.html")


def movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, template_name="movies.html", context=context)


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie = Movie.objects.get(id=pk)
        context = {'movie': movie}
        return render(request, 'movie.html', context)
    return movies(request)



def genres(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request,'genres.html',context)

def genre(request, pk):
    genre = Genre.objects.get(id=pk)
    movies = Movie.objects.filter(genre__id=pk)
    context = {'genre': genre, 'movies': movies}
    return render(request, "movies_by_genres.html", context)
