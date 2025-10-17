from django.shortcuts import render, HttpResponse
import re
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.http import JsonResponse
import json

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

def get_ai_remedy(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        illness = data.get('illness', '').lower()
        age = data.get('age', '')
        duration = data.get('duration', '').lower()

        remedies = {}
            #'headache': 'Peppermint tea, Ginger tea',
            #'stress': 'Ashwagandha, Lavender oil',
            #'insomnia': 'Valerian root, Chamomile tea',
            #'fatigue': 'Ginseng, Rhodiola rosea',
            #'cold': 'Try Tulsi tea twice a day and inhale steam with eucalyptus oil, Echinacea',
        
        
        yoga ={}
            #'weight loss': 'Surya Namaskar, Warrior Pose, Boat Pose',
            #'flexibility': 'Downward Dog, Cat-Cow Stretch, Seated Forward Bend',
            #'stress relief': 'Child\'s Pose, Legs-Up-The-Wall Pose, Corpse Pose',
            #'strength building': 'Plank Pose, Chair Pose, Bridge Pose'
            
        

        if illness == "cold":
            remedies["cold"] = "Tulsi tea twice a day and inhale steam with eucalyptus oil, Echinacea"
            yoga["cold"] = "Anulom Vilom Pranayama, Bhujangasana (Cobra Pose), Setu Bandhasana (Bridge Pose)"
        elif illness == "headache":
            remedies["headache"] = "Peppermint tea, Ginger tea"
            yoga["headache"] = "Adho Mukha Svanasana (Downward-Facing Dog), Balasana (Child's Pose), Uttanasana (Standing Forward Bend)"
        elif illness == "stress":
            remedies["stress"] = "Ashwagandha, Lavender oil"
            yoga["stress"] = "Sukhasana (Easy Pose) with deep breathing, Viparita Karani (Legs-Up-The-Wall Pose), Savasana (Corpse Pose)"
        elif illness == "insomnia":
            remedies["insomnia"] = "Valerian root, Chamomile tea"
            yoga["insomnia"] = "Supta Baddha Konasana (Reclining Bound Angle Pose), Viparita Karani (Legs-Up-The-Wall Pose), Savasana (Corpse Pose)"
        else:
            remedies[illness] = "No specific herbal remedy found for your symptoms. Consider consulting a healthcare professional."
            yoga[duration] = "No specific yoga plan found for your goal. Consider consulting a yoga instructor."

        response = {
            "remedies": remedies,
            "yoga": yoga,
        }

       # herbs = remedies.get(illness, 'No specific herbal ' \
        #'remedy found for your symptoms. Consider consulting a healthcare professional.')

        #yoga_plans = yoga.get(duration, 'No specific yoga plan found for your goal. ' \
        #'Consider consulting a yoga instructor.')

        #plan = f"""
        #<h3>Personalized Herbal Remedy and Yoga Plan</h3>
        #<p><strong>symptoms:</strong> {illness}</p>
        #<p><strong>Herbal Remedies:</strong> {herbs}</p>
        #<p><strong>yoga/Exercise:</strong> {yoga_plans}</p>
        #<p><strong>Diet Tip:</strong> Eat more seasonal fruits and stay hydrated.</p>
        #"""
        return JsonResponse(response)
    return JsonResponse({"error": "Invalid request method."}, status=400)