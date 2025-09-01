from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is the home page of Herbal Harmony Backend')

def about(request):
    return HttpResponse('This is the about page of Herbal Harmony Backend')
