from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location, Category


# Create your views here.

def welcome(request):
    return render(request, 'index.html')



def index(request):
    images = Image.get_all_images()

    return render(request, 'index.html', {"images": images})
