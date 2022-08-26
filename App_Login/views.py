from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import SignUpForm,LoginForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from App_Login.models import UserProfile,Follow
from App_Login.forms import EditProfile
from App_Post.forms import PostForm
from django.contrib.auth.models import User


# Create your views here.
def Sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form =  SignUpForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            # return HttpResponseRedirect(reverse('App_Login:login'))
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
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_Post:home'))

    return render(request,'App_Login/profile.html',context={'form':form})

@login_required
def Edit_Profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == "POST":
        form = EditProfile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/edit_profile.html',context={'form':form,'title':'Edit Profile'})


@login_required
def Other_user(request,username):
    other_user = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user,following=other_user)
    if other_user == request.user:
        return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/other_user.html',context={'other_user':other_user,'already_followed':already_followed})     


@login_required
def follow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(following=following_user,follower=follower_user)
    if not already_followed:
        followed_user = Follow(following=following_user,follower=follower_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_Login:other-user',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(following=following_user,follower=follower_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_Login:other-user',kwargs={'username':username}))
    