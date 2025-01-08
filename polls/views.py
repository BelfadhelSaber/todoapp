from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.utils.translation import gettext as _
from .models import User, Todo

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
def contact(request):
    return render(request,'polls/contact.html',{})


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
def contactus(request):
    name=request.child


