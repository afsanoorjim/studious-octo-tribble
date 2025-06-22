from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

def signup(request):
    return HttpResponse("This is Signup Page")

def login(request):
    return HttpResponse("This is Login Page")
