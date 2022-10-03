from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet

def home(request):
    return HttpResponse("<h1>This is the home page!</h1>")

def pet_detail(request, pet_id):
    return HttpResponse(F"<h1>Pet Number: {pet_id}</h1>")