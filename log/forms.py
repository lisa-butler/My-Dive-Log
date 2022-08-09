from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['date', 'location', 'depth', 'time', 'buddy', 'note']
        widgets = {
            'date' : forms.TextInput(attrs={'class': 'form-control'}),
            'location' : forms.TextInput(attrs={'class': 'form-control'}),
        }
