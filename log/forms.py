from django import forms
from .models import Item


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
