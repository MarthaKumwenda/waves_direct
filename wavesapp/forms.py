from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Popup, Comment,Images, Gallery


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,required=True)
    last_name = forms.CharField(max_length=32,required=True)
    email = forms.EmailField(required=True,max_length=100)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class ProfileForm(forms.ModelForm):
    uploadphoto = forms.FileField()
    company_name = forms.CharField(max_length=32,required=True)
    phone = forms.CharField(max_length = 15)
    address = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 15)
    email = forms.EmailField(required=True,max_length=100)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    Services_offered = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ['uploadphoto','company_name', 'email', 'phone', 'city', 'address','role','Services_offered']

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class GalleryForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = Gallery
        fields = ('title', 'body', )
class ImageForm(forms.ModelForm):
    image = forms.FileField()
    class Meta:
        model = Images
        fields = ('image', )
