from django.urls import path,include
from .views import loginview, logoutview, registerview,homeview

urlpatterns = [
    path('home/',homeview,name='home'),
    path('login/',loginview,name='login'),
    path('home/logout/',logoutview,name='logout'),
    path('login/register/',registerview,name='register'),
]