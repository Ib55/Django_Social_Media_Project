from django.urls import path
from .import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/',views.Sign_up,name='signup'),
    path('login/',views.Login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.Profile,name='profile'),
    path('edit-profile/',views.Edit_Profile,name='edit_profile'),
    path('other_user/<username>',views.Other_user,name='other-user'),
    path('follow/<username>',views.follow,name='follow'),
    path('unfollow/<username>',views.unfollow,name='unfollow')
]
