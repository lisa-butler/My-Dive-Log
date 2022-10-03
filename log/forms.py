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
            'date': forms.DateInput(attrs={'class': 'form-inputs', 'type': 'date', 'id': 'date-input'}),
            'location': forms.TextInput(attrs={'class': 'form-inputs'}),
            'depth': forms.TextInput(attrs={'class': 'form-inputs'}),
            'time': forms.TextInput(attrs={'class': 'form-inputs'}),
            'buddy': forms.TextInput(attrs={'class': 'form-inputs'}),
            'note': forms.TextInput(attrs={'class': 'form-inputs'})
        }




class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
