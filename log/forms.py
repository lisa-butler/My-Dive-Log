from django import forms
from .models import Item
from allauth.account.forms import SignupForm


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



class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['organization'] = forms.CharField(required=True)
    def save(self, request):
        organization = self.cleaned_data.pop('organization')
        ...
        user = super(MyCustomSignupForm, self).save(request)

# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=12, label='First Name')
#     last_name = forms.CharField(max_length=12, label='Last Name')
#     email = forms.EmailField(max_length=20, label='Email')
#     dive_club = forms.CharField(max_length=12, label='Dive Club')
#     password = forms.CharField(max_length=12, label='Password')

#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.fist_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.password = self.cleaned_data['password']
#         user.save()
#         return user
