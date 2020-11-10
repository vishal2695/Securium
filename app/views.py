from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .forms import userloginfrm, usersignupfrm
from .models import Products
from django.contrib import messages
# Create your views here.

def home(request):
    item = Products.objects.all()
    return render(request, 'app/home.html', {'items':item})


def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            fm = userloginfrm(request.POST)
            if fm.is_valid():
                a = fm.cleaned_data['username']
                b = fm.cleaned_data['password']

                user = auth.authenticate(username=a, password=b)
                if user is not None:
                    auth.login(request, user)
                    messages.info(request, 'You are logged In Successfully..!!')
                    return HttpResponseRedirect('/home/')
                else:
                    messages.info(request, 'Invalid credential')
        else:
            fm = userloginfrm()
        return render(request, 'app/login.html', {'fm': fm})

def usersignup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            fm = usersignupfrm(request.POST)
            if fm.is_valid():
                a = fm.cleaned_data['username']
                b = fm.cleaned_data['first_name']
                c = fm.cleaned_data['last_name']
                d = fm.cleaned_data['email']
                e = fm.cleaned_data['password']
                g = fm.cleaned_data['password2']
                if e == g:
                    f = User.objects.create_user(username=a, first_name=b, last_name=c, email=d, password=e)
                    f.save()
                    messages.success(request, 'You are Successfully Registered..!!')
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, 'Password not matched')
        else:
            fm = usersignupfrm()
        return render(request, 'app/signup.html', {'fm': fm})

def userlogout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
