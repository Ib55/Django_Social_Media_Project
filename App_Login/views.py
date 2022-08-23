from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import SignUpForm,LoginForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def Sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form =  SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request,'App_Login/signup.html',context={'form':form,'registered':registered})

def Login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Post:home'))
    return render(request,'App_Login/login.html',context={'form':form,'title':'Login Page'})

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def Profile(request):
    return render(request,'App_Login/profile.html')