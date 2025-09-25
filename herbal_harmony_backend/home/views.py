from django.shortcuts import render, HttpResponse
import re
from django.utils.html import escape
from django.utils.safestring import mark_safe

# Create your views here.
#def index(request):
    #return render(request, 'index.html')
    #return HttpResponse('This is the home page of Herbal Harmony Backend')

#def about(request):
    #return HttpResponse('This is the about page of Herbal Harmony Backend')



def Home(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def yoga(request):
    return render(request, 'yoga.html')

def herb(request):
    return render(request, 'herb.html')

def medherb(request):
    return render(request, 'medherb.html')

def childyoga(request):
    return render(request, 'childyoga.html')
