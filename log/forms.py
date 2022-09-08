from django import forms
from django.contrib.auth.models import User
from .models import Item
from django.contrib.auth.forms import UserCreationForm




class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['date', 'location', 'depth', 'time', 'buddy', 'note']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-inputs'}),
            'location': forms.TextInput(attrs={'class': 'form-inputs'}),
            'depth': forms.TextInput(attrs={'class': 'form-inputs'}),
            'time': forms.TextInput(attrs={'class': 'form-inputs'}),
            'buddy': forms.TextInput(attrs={'class': 'form-inputs'}),
            'note': forms.TextInput(attrs={'class': 'form-inputs'})
        }


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))


