from django.urls import path
from .import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/',views.Sign_up,name='signup'),
    path('login/',views.Login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.Profile,name='profile')
]
