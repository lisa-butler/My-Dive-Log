from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_logpage(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "log/logpage.html", context)
 

def log_a_dive(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        # date = request.POST.get('item_date')
        # location = request.POST.get('item_location')
        # depth = request.POST.get('item_depth')
        # time = request.POST.get('item_time')
        # buddy = request.POST.get('item_buddy')
        # note = request.POST.get('item_note')
        # Item.objects.create(date=date, location=location, depth=depth, time=time, buddy=buddy, note=note)
        
        return redirect('get_logpage')
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, "log/logadive.html", context)

