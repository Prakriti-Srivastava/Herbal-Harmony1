from django.contrib import admin
from django.urls import path
from home import views
from . import views

urlpatterns = [
   #path('', views.index, name='home'),
  # path("about", views.about, name='about'),
   path("yoga", views.yoga, name='yoga'),
   #path("index", views.index, name='index'),
   path('', views.Home, name='Home'),
   path('About', views.About, name='About'),
   
]