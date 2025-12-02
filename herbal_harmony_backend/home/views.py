from django.shortcuts import render, HttpResponse
import re
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.http import JsonResponse
import json

from .form import HealthForm 
from .ai import getRemedyAndYoga



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

def ai(request):
    return render(request, 'ai.html')

def healthform(request):
    print("Entered healthform view")   # line after def healthform(request):
    result = None
    if request.method == 'POST':
        form = HealthForm(request.POST)
        

        if form.is_valid():

            age_group = form.cleaned_data['age_group']
            symptom = form.cleaned_data['symptom']
            # print("Age Group : ", age_group)
            # print("Symptom : ", symptom)
            print("Form inputs:",(age_group, symptom))
            result = getRemedyAndYoga(age_group, symptom)
            print("AI function returned:", result)
            # print("Form inputs received:", age_group, symptom)
            # print("Result : ", result)
        


            if result:     
                return render(request, 'output.html', {
                    'age': age_group,
                    'symptom': symptom,
                    'remedy': result['remedy'],
                    'yoga': result['yoga'],
                    'link_remedy': result['link_remedy'],
                    'link_yoga': result['link_yoga']
                })
            else:
                return render(request, 'output.html', {
                    'error': 'No matching remedy found for your input. Try again!'
                })
            
            # response_message = f"Form submitted successfully! Age Group: {age_group}, Symptom: {symptom}"
            # return render(request, 'output.html', {'Age Group': age_group, 'Symptom': symptom})
    else:
        form = HealthForm()
    return render(request, 'healthform.html', {'form': form})

def tulsi(request):
    return render(request,'tulsi.html')

def kapalbhati(request):
    return render(request,'kapalbhati.html')

def Treatment(request):
    return render(request,'Treatment.html')

def Fever(request):
    return render(request,'Fever.html')
def Cold(request):
    return render(request,'Cold.html')
def bodypain(request):
    return render(request,'bodypain.html')
def Headache(request):
    return render(request,'Headache.html')
def Fatigue(request):
    return render(request,'Fatigue.html')

def basic(request):
    return render(request,'basic.html')

def tadasana(request):
    return render(request,'tadasana.html')

def setubandhasana(request):
    return render(request, 'setubandhasana.html')

def teenager(request):
    return render(request, 'teenager.html')

def kapalbhatiadult(request):
    return render(request, 'kapalbhatiadult.html')

def padmasana(request):
    return render(request, 'padmasana.html')

def viparitakarani(request):
    return render(request, 'viparitakarani.html')

def adhomukhasvanasana(request):
    return render(request, 'adhomukhasvanasana.html')

def sukhasana(request):
    return render(request, 'sukhasana.html')

def suryana(request):
    return render(request, 'suryana.html')

def adult(request):
    return render(request, 'adult.html')

def pranayama(request):
    return render(request, 'pranayama.html')

def bhujangasana(request):
    return render(request, 'bhujangasana.html')

def dhanurasana(request):
    return render(request, 'dhanurasana.html')

def vrikshasana(request):
    return render(request, 'vrikshasana.html')

def anulomvilom(request):
    return render(request, 'anulomvilom.html')

def middleage(request):
    return render(request, 'middleage.html')

def shavasana(request):
    return render(request, 'shavasana.html')

def shashankasana(request):
    return render(request, 'shashankasana.html')

def ardhamatsyendrasana(request):
    return render(request, 'ardhamatsyendrasana.html')

def ustrasana(request):
    return render(request, 'ustrasana.html')

def trikonasana(request):
    return render(request, 'trikonasana.html')

def apanasana(request):
    return render(request, 'apanasana.html')

def seniors(request):
    return render(request, 'seniors.html')

def pavanamuktasana(request):
    return render(request, 'pavanamuktasana.html')

def suptabaddhakonasana(request):
    return render(request, 'suptabaddhakonasana.html')

def mentalhealth(request):
    return render(request, 'mentalhealth.html')

def aromaherb(request):
    return render(request, 'aromaherb.html')
def culinherb(request):
    return render(request, 'culinherb.html')

def baddhakonasana(request):
    return render(request, 'baddhakonasana.html')

def animalandfun(request):
    return render(request, 'animalandfun.html')

def marjariasana(request):
    return render(request, 'marjariasana.html')

def simhasana(request):
    return render(request, 'simhasana.html')

def mandukasana(request):
    return render(request, 'mandukasana.html')

def matsyasana(request):
    return render(request, 'matsyasana.html')

def weakness(request):
    return render(request, 'weakness.html')