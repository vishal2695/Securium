from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from .forms import userloginfrm, usersignupfrm
from .models import Products, Cartitem
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url=('/'))
def home(request):
    item = Products.objects.all()
    gg = request.session.get('key')
    if gg == None:
        request.session['key'] = 0
    items = Cartitem.objects.filter(cuser=request.user) 
    ff = len(items)
    request.session['key'] = ff
    return render(request, 'app/home.html', {'items':item})

@login_required(login_url=('/'))
def preview(request, id):
    item = get_object_or_404(Products, id=id)
    return render(request, 'app/show.html', {'item':item})

@login_required(login_url=('/'))
def addcart(request, id):
    product = get_object_or_404(Products, id=id)
    cart = Cartitem.objects.create(items=product, cuser=request.user)
    cart.save()
    items = Cartitem.objects.filter(cuser=request.user) 
    ff = len(items)
    request.session['key'] =  ff
    
    messages.success(request, 'Item is successfully added to your cart..!!')
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url=('/'))
def billing(request, id):
    item = get_object_or_404(Products, id=id)
    total = item.price
    print(item.price)
    return render(request, 'app/cart.html',{'ittem':item,'total':total})

@login_required(login_url=('/'))
def showcart(request):
    items = Cartitem.objects.filter(cuser=request.user) 
    ff = len(items)
    request.session['key'] =  ff 
    
    print(ff)
    total = 0.00
    for item in items:
        total += float(item.items.price)
        # new_total = 'total'
        print(total)
    print(total)
    return render(request, 'app/cart.html', {'items':items, 'total':total})

@login_required(login_url=('/'))
def remove(request,id):
    item = get_object_or_404(Cartitem, id=id)
    item.delete()
    return HttpResponseRedirect(reverse('cart'))

@login_required(login_url=('/'))
def end(request):
    return render(request, 'app/success.html')


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
                    request.session.create()
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
