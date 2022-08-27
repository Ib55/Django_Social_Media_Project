from django.urls import path
from . import views


app_name = 'App_Post'

urlpatterns = [
    path('',views.Home,name='home'),
    path('like/<pk>/',views.Like_Post,name='like'),
    path('unlike/<pk>/',views.unlike,name='unlike')
]
