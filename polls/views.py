from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.conf import settings
from django.core.paginator import Paginator

from django.utils.translation import gettext as _
from .models import User, Todo,Contact,Hotel,Checkout

@login_required
def index(request):
    print('test')
    return render(request,'polls/home.html',{})

    return HttpResponse("Hello,ddd world. You're at the polls index.")


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            return redirect('login')
        
    return render(request,'polls/login.html',{})


def signup(request):

    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        print(email,password)
        user = User.objects.create(email=email,password=password,username=username)
        user.save()
    return render(request,'polls/signup.html',{})
    return HttpResponse("Hello, world. You're at the polls index.")
def LogoutView(request):
    logout(request)
    return redirect('login')
#@login_required
def home(request):
   
    return render(request,'polls/home.html',{})
@login_required



def todo(request):
    todos = Todo.objects.all()
    if request.method == 'POST' :
        title = request.POST.get('title')
        value = request.POST.get('value')
        
        print(title,value)
        todo = Todo.objects.create(title=title,value=value)
        todo.save()
    return render(request,'polls/todo.html',{'todos':todos})
def deletetodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo')

def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name,email,message)
        contact = Contact.objects.create(name=name,email=email,message=message)
        contact.save()
    return render(request,'polls/contact.html',{'contacts':contacts})


def checkout(request,hotel_id):
    checkouts = Contact.objects.all()
    if request.method == 'POST' :
        email=request.POST.get('email')
        adresse=request.POST.get('adresse')
        ville=request.POST.get('ville')
        pays=request.POST.get('pays')
        zipcode=request.POST.get('zipcode')
        nbpersonne=request.POST.get('nbpersonne')
        nbenfant=request.POST.get('nbenfant')
        ch=Checkout.objects.create(email=email,adresse=adresse,ville=ville,pays=pays,zipcode=zipcode,nbpersonne=nbpersonne,nbenfant=nbenfant)
        print(ville)
        ch.save()
    hotel=Hotel.objects.get(pk=hotel_id)
    return render(request,'polls/checkout.html',{'checkouts':checkouts,'hotel':hotel})

def hotel(request):
    product_object=Hotel.objects.all()
    item_name =request.GET.get('item-name')
    if item_name!='' and item_name is not None:
        product_object=Hotel.objects.filter(title__icontains=item_name)#icontains=like sql
    paginator=Paginator(product_object, 4)
    page=request.GET.get('page')
    product_object =paginator.get_page(page)
    return render(request, 'polls/home.html',{'product_object':product_object})

def set_language(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return response
def bienvenu(request):
        return render(request, 'polls/bienvenu.html')

def detail(request):
    return render(request, 'polls/datail.html')

