from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Post
#
# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('title', 'text',)

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,required=True)
    last_name = forms.CharField(max_length=32,required=True)
    email = forms.EmailField(required=True,max_length=100)
    # bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
