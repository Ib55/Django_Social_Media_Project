
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from App_Login.models import UserProfile

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username','style':'margin-bottom:10px'}))
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email','style':'margin-bottom:10px'}))
    password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password','style':'margin-bottom:10px'}))
    password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Again Password'}))
    class Meta:
         model = User
         fields = ('username','email','password1','password2')

   


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username','style':'margin-bottom:10px'}))
    password = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
         model = User
         fields = ('username','password')

   
class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = UserProfile()
        exclude = ('user',)