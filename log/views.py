from django.shortcuts import render
from .models import Item

# Create your views here.


def get_logpage(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "log/logpage.html", context)
 

def log_a_dive(request):
    return render(request, "log/logadive.html")

