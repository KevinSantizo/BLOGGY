from django.urls import path
from . import views

app_name = 'bloggi'
urlpatterns = [
    path('blog-home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
