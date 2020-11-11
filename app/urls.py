from django.urls import path
from app import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.usersignup, name='signup'),
    path('', views.userlogin, name='login'),
    path('log/', views.userlogout, name='logout'),
    path('show/<int:id>', views.preview, name='show'),
    path('add/<int:id>', views.addcart, name='add'),
    path('pay/<int:id>', views.billing, name='bill'),
    path('cart/', views.showcart, name='cart'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('Success/', views.end, name='end')
]