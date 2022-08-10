from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['date', 'location', 'depth', 'time', 'buddy', 'note']
        widgets = {
            'date' : forms.TextInput(attrs={'class': 'form-inputs'}),
            'location' : forms.TextInput(attrs={'class': 'form-control'}),
            'depth' : forms.TextInput(attrs={'class': 'form-control'}),
            'time' : forms.TextInput(attrs={'class': 'form-control'}),
            'buddy' : forms.TextInput(attrs={'class': 'form-control'}),
            'note' : forms.TextInput(attrs={'class': 'form-control'}),
        }
