from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class profileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
    

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=10)
    mobile =forms.CharField(max_length=10)
    sex =forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','phone','mobile','sex', 'password1', 'password2',)
