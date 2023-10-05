from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def ale(request):
    return HttpResponse("Hello, Alejandro!")

def caro(request):
    return HttpResponse("Hello, Caro!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}")
    