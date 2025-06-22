from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def landing_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'landing_page.html', context)

def signup(request):
    return HttpResponse("This is Signup Page")

def login(request):
    return HttpResponse("This is Login Page")
