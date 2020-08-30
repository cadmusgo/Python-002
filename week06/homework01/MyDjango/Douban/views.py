from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
from .models import MovieComment

def index(request):
    return render(request, 'movie.html', locals())

def movie_comments(request):
    condtions = {'n_star__gt': 3}
    comments = MovieComment.objects.filter(**condtions)
    print("xxx")
    print(comments)
    return render(request, 'movie_comments.html', locals())

