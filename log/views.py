from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

@login_required
def get_logpage(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "logpage.html", context)
    

def index(request):
    return render(request, 'index.html')

@login_required
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
    return render(request, "logadive.html", context)


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
    return render(request, 'edit_item.html', context)

    
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # if request.method == "POST":
    item.delete()
    return redirect('get_logpage')


def get_home(request):
    return render(request, 'index.html')


def logout(request):
    return render(request, 'logout.html')


def register_user(request):
    
    form = RegisterUserForm(request.POST)

    if request.method == "GET":
        return render(request, 'registration/register_user.html', {
            'form': form,
            })

    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('get_home')
        else:
            form = RegisterUserForm()
