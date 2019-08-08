from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Kevito',
        'title': 'My first blog 1',
        'content': 'First post content',
        'date_posted': 'August, 07, 2019'
    },
    {
        'author': 'Papusho',
        'title': 'My second blog 2',
        'content': 'Second post content',
        'date_posted': 'August, 08, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'bloggi/home.html', context)


def about(request):
    return render(request, 'bloggi/about.html', {'title': 'About Blog!!!'})
