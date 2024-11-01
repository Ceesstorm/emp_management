from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from emp import models
from emp.models import Truck

# - Register/Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - Login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# Truck form
class TruckForm(forms.ModelForm):
    class Meta:
        model = models.Truck
        fields = ['day', 'departure_time', 'tender', 'truck_number', 'origin', 'destination', 'operator', 'country', 'company', 'street', 'city', 'postal_code', 'city', 'phone_number']
        widgets = {
            'departure_time': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
                'placeholder': 'HH:MM'
            }),
        }

    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departure_time'].input_formats = ['%H:%M']

class AddTruckForm(forms.ModelForm):
    class Meta:
        model = models.Truck
        fields = ['day', 'departure_time', 'tender', 'truck_number', 'origin', 'destination', 'operator', 'country', 'company', 'street', 'city', 'postal_code', 'city', 'phone_number']

        widgets = {
            'departure_time': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
                'placeholder': 'HH:MM'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departure_time'].input_formats = ['%H:%M']
    
