from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Pet

def home(request):
    #return HttpResponse("<h1>This is the home page!</h1>")
    pets = Pet.objects.all()
    return render(request, 'home.html',{'pets':pets,})

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except:
        raise Http404("No pet associated with that ID number")
    return render(request, 'pet_detail.html', {'pet':pet,})