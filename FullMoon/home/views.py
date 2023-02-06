
from django.shortcuts import render
from .models import Herbs
from django.views import View
# Create your views here.

    

def herb_list(request):
    herbs = Herbs.objects.all()
    context = {
        "herbs":herbs
    }

    return render(request, "herb.html", context)

def herb_view(request, pk):
    listing = Herbs.objects.get(id = pk)

    context = {
        "listing": listing
    }
    return render(request, "listings.html", context)

def home(request):
    return render(request, "base.html")

