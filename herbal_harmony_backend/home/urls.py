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
   path('childyoga', views.childyoga, name='childyoga'),
   path('ai', views.ai, name='ai'),
   path('get_ai_remedy', views.get_ai_remedy, name='get_ai_remedy'),
   path('healthform', views.healthform, name='healthform'),
   path('tulsi', views.tulsi, name='tulsi'),
   path('kapalbhati', views.kapalbhati, name='kapalbhati'),
   path('Treatment', views.Treatment, name='Treatment'),
   path('Fever', views.Fever, name='Fever'),
   path('Cold', views.Cold, name='Cold'),
   path('Bodypain', views.Bodypain, name='Bodypain'),
   path('Headache', views.Headache, name='Headache'),
   path('Fatigue', views.Fatigue, name='Fatigue'),
]