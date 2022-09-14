from django import forms
from django.contrib.auth.models import User
from .models import Item, Info
from django.contrib.auth.forms import UserCreationForm




class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['username', 'date', 'location', 'depth', 'time', 'buddy', 'note']
        widgets = {
            'username': forms.HiddenInput(),
            'date': forms.TextInput(attrs={'class': 'form-inputs'}),
            'location': forms.TextInput(attrs={'class': 'form-inputs'}),
            'depth': forms.TextInput(attrs={'class': 'form-inputs'}),
            'time': forms.TextInput(attrs={'class': 'form-inputs'}),
            'buddy': forms.TextInput(attrs={'class': 'form-inputs'}),
            'note': forms.TextInput(attrs={'class': 'form-inputs'})
        }


class RegisterUserForm(UserCreationForm):
    model = Info
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

