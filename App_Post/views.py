
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_Login.models import Follow
from App_Post.models import Post,Like
from django.urls import reverse
# Create your views here.
@login_required
def Home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in = following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post',flat=True)
    if request.method == 'GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    return render(request,'App_Post/home.html',context={'search':search,'result':result,'posts':posts,'liked_post_list':liked_post_list})

@login_required
def Like_Post(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        like = Like(post=post,user=request.user)
        like.save()
        return HttpResponseRedirect(reverse('App_Post:home'))



@login_required
def unlike(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Post:home'))