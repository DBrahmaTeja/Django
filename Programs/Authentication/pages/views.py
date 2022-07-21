import django
from django.shortcuts import redirect, render
from . forms import CreateUserForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method=='POST':
       # form=UserCreationForm(data=request.POST)
        form=CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            #redirect to index page if it is successful
    else:
        #form=UserCreationForm()
        form=CreateUserForm()
    return render(request,'pages/register.html',{'form': form})

def dashboard(request):
    return render(request,'pages/dashboard.html')
def login(request):
    if request.method=='POST':
        #if the user exists with given credentials
        username =request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            #login the user
            auth_login(request,user)
            # redirect to dashboard
            return redirect('dashboard')
        #login
        else:
            #provide some error message
            messages.error(request,'Username or Password is incorrect')
            return render(request,'pages/login.html')
    else:
        return render(request,'pages/login.html')



