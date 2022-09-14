from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, AbstractUser, Permission
from django.contrib import messages



# Create your views here.

@login_required
def get_logpage(request):
    items = Item.objects.filter(username=request.user)
    context = {
        'items': items
    }
    return render(request, "logpage.html", context)

@login_required
def get_club_logs(request):
    items = Item.objects.all()
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


def diving_officer_home(request):
    return render(request, 'diving_officer.html')      


# @permission_required('diving_officer.can_view')      





# def show_do_view(request):
#     do_view = ''
#     if request.groups == 'Diving_Officer':
#         do_view = RegisterUserForm(request.POST)             


# def group_required(Diving_Officer):
#     """Requires user membership in at least one of the groups passed in."""
#     def in_groups(user):
#         if user.groups.filter(name='Diving_Officer').exists():
#             print('---working---')

#         else:
#             print('---not working---')
     

#     return user_passes_test(in_groups, login_url='403')


# @group_required('Diving_Officer')
# def diving_officer_home(request):
#     return render(request, 'diving_officer.html')  

    #    if user.is_authenticated:
    #         print('------1------', user.groups)
    #         if (user.groups.filter(name__in=Diving_Officer)):
    #             print('-----2-----')
    #             return True
    #     return False

