from django.shortcuts import render
from django.http import HttpResponse
from bloggi.models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bloggi/home.html', context)


def about(request):
    return render(request, 'bloggi/about.html', {'title': 'About Blog!!!'})
