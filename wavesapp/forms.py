from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Popup

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,required=True)
    last_name = forms.CharField(max_length=32,required=True)
    email = forms.EmailField(required=True,max_length=100)
#
# class PopupForm(UserCreationForm):
#     first_name = forms.CharField(max_length=32,required=True)
#     last_name = forms.CharField(max_length=32,required=True)
#     email = forms.EmailField(required=True,max_length=100)


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class PopupForm(forms.ModelForm):
    client_name = forms.CharField(max_length=60,required=True)
    phone_number = forms.CharField(max_length=30)
    email = forms.EmailField(required=True,max_length=100)
    time_of_appointment = forms.TimeField()
    due_date = forms.DateField()
    request = forms.CharField(max_length = 2000)

    class Meta:
        model = Popup
        fields = ('client_name','phone_number','email','time_of_appointment','due_date','request')
