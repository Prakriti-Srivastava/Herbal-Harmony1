from django.contrib import admin
from django.urls import path
from home import views
from . import views

urlpatterns = [
   #path('', views.index, name='home'),
  # path("about", views.about, name='about'),
   #path("index", views.index, name='index'),
   path("yoga", views.yoga, name='yoga'),
   path('', views.Home, name='Home'),
   path('About', views.About, name='About'),
   path('herb', views.herb, name='herb'),
   path('medherb', views.medherb, name='medherb'),
   path('childyoga', views.childyoga, name='childyoga')
   
]