from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LibraryCardForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def catalog(request):
    return render(request, 'website/catalog.html')

def library_card_view(request):
    if request.method == "POST":
        form = LibraryCardForm(request.POST)
        if form.is_valid():
            library_card = form.save(commit=False)
            library_card.owner = request.user
            library_card.save()
            messages.success(request, f'Card created! {library_card}')
            return redirect('/')
    else:
        form = LibraryCardForm()


    return render(request, "website/librarycard.html", {'form':form})