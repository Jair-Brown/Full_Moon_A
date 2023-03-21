
from django.shortcuts import render
from .models import Herbs
from django.views import View
# Create your views here.



def herb_list(request):
    # returns a list of herbs in database
    herbs = Herbs.objects.all()
    context = {
        "herbs":herbs
    }

    return render(request, "listings.html", context)

def herb_view(request, name):
    # returns specific herb from database with uses
  herb = Herbs.objects.get(name = name)
  context = {"herb": herb}
  return render(request, "herb.html", context)

def home(request):
    return render(request, "base.html")

