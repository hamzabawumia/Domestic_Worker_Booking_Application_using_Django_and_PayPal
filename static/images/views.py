from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from home.models import Contact
from home.models import Login
from home.models import Signup
from django.contrib import messages
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {
        "variable":"this is all about me"
    }
   # return HttpResponse('this is home page')
    return render(request,'index.html', context)

@login_required(login_url='login')
def products(request):
    return render(request,'products.html')

@login_required(login_url='login')
def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')

@login_required(login_url='login')
def cook(request):
    return render(request,'cook.html')

@login_required(login_url='login')
def elderly(request):
    return render(request,'elderly.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def services(request):
    return render(request,'services.html')

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password =request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully logged in')
                    return redirect('/')
                else:
                    messages.info(request, 'Username Or password is incorrect')
            context = {}
            return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.warning(request,"Account successfully logout")
    return redirect('login')


def signup(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'signup.html', context)