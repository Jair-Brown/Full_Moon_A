
from django.shortcuts import render
from .models import Herbs
from django.views.generic import ListView
from django.db.models import Q


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
     return render (request, "base.html")


class SearchResultsView(ListView):
    model = Herbs
    context_object_name = "quotes"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list =  Herbs.objects.filter(
            Q(name__icontains=query) | Q(uses__icontains=query)
        )
    
        
        if object_list.exists():
            return object_list
        
        else:
             return "sorry nothing here"


     
     
     

