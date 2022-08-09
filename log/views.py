from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_logpage(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "log/logpage.html", context)

def index(request):
    return render(request, 'log/index.html')

def log_a_dive(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_logpage')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, "log/logadive.html", context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_logpage')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'log/edit_item.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_logpage')
