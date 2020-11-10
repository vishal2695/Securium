from django.urls import path
from app import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.usersignup, name='signup'),
    path('', views.userlogin, name='login'),
    path('log/', views.userlogout, name='logout'),
]