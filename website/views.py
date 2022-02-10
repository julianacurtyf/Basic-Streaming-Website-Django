from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from streaming.models import Movie, Course, TVShow, Episode, Actor, Class, Client, Payment, Subscription


def welcome(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, "website/welcome.html",
                  {"client": client,
                   "movies": Movie.objects.all(),
                   "series": TVShow.objects.all()})


def login(request):
    return render(request, "website/login.html",
                  {"clients": Client.objects.all()})


def allmovies(request, id_client):
    client = get_object_or_404(Client, pk=id_client)
    return render(request, "website/allmovies.html",
                  {"client": client,
                   "movies": Movie.objects.all()})


def allcourses(request, id_client):
    client = get_object_or_404(Client, pk=id_client)
    return render(request, "website/allcourses.html",
                  {"client": client,
                   "courses": Course.objects.all()})


def alltvshows(request, id_client):
    client = get_object_or_404(Client, pk=id_client)
    return render(request, "website/alltvshows.html",
                  {"client": client,
                   "tvshows": TVShow.objects.all()})


def movie(request, id_client, id):
    client = get_object_or_404(Client, pk=id_client)
    movie_part = get_object_or_404(Movie, pk=id)
    return render(request, "website/movie.html",
                  {"client": client,
                   "movie": movie_part,
                   "actors": Actor.objects.all()})


def tvshow(request, id_client, id):
    client = get_object_or_404(Client, pk=id_client)
    tvshow_part = get_object_or_404(TVShow, pk=id)
    return render(request, "website/tvshow.html",
                  {"client": client,
                   "tvshow": tvshow_part,
                   "episodes": Episode.objects.all()})


def course(request, id_client, id):
    client = get_object_or_404(Client, pk=id_client)
    course_part = get_object_or_404(Course, pk=id)
    return render(request, "website/course.html",
                  {"client": client,
                   "course": course_part,
                   "classes": Class.objects.all()})
