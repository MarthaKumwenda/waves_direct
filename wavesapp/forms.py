from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,required=True)
    last_name = forms.CharField(max_length=32,required=True)
    email = forms.EmailField(required=True,max_length=100)


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class ProfileForm(forms.ModelForm):
    company_name = forms.CharField(max_length=32,required=True)
    photo = forms.ImageField()
    email = forms.EmailField(required=True,max_length=100)
    phone = forms.CharField(max_length = 15)
    location = forms.CharField(max_length = 15)
    address = forms.CharField(max_length = 100)

    class Meta:
        model = Profile
        fields = ['company_name', 'email', 'phone', 'location', 'address']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
