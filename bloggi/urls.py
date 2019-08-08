from django.urls import path
from . import views

app_name = 'bloggi'
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]