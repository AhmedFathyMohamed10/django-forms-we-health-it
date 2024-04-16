from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password'
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    labels = {
        'username': 'Username',
        'password': 'Password'
    }
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'first_name',
            'last_name',
            'bio',
            'location'
        ]
