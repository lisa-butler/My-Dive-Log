from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Info
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.shortcuts import redirect



# Create your views here.

@login_required
def get_logpage(request):
    items = Item.objects.filter(username=request.user).order_by('-date')
    context = {
        'items': items
    }
    return render(request, "logpage.html", context)

@login_required
def get_club_logs(request):
    items = Item.objects.all().order_by('-date')
    context = {
        'items': items
    }
    return render(request, "club_logpage.html", context)


def index(request):
    return render(request, 'index.html')

@login_required
def log_a_dive(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            cleaned_form = form.clean()
            cleaned_form['username'] = request.user
            new_form = ItemForm(cleaned_form)
            # request.user.DiveLog_set.Create(name=n)
            new_form.save()
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


def register_request(request):
    currentForm = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        currentForm = form
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("get_home")
        # else:
            # messages.error(request, form.errors.a())
    form = NewUserForm()
    return render (request=request, template_name="registration/register_user.html", context={"register_form":currentForm})



def diving_officer_home(request):
    return render(request, 'diving_officer.html')


def club_members(request):
    all_users = User.objects.values()

    context = {
        'allUsers': all_users
    }

    return render(request, 'club_members.html', context)


# def edit_member(request, user):
#     user = get_object_or_404(user, id=user)
#     if request.method == 'POST':
#         form = NewUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('')
#     form = NewUserForm(instance=user)
#     context = {
#         'form': form
#     }
#     return render(request, 'edit_member', context)

