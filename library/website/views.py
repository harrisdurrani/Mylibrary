from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def catalog(request):
    return render(request, 'website/catalog.html')

def library_card_view(request):
    return render(request, "website/librarycard.html")