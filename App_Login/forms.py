
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Again Password'}))
    class Meta:
         model = User
         fields = ('username','email','password1','password2')

   


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
         model = User
         fields = ('username','password')

   