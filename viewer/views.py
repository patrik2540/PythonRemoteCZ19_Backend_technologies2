from django.http import HttpResponse
from django.shortcuts import render

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
