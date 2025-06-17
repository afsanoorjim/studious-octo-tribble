from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing_page(request):
    return HttpResponse("This is Landing Page") 