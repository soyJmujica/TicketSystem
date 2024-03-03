from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def homeTC(request):
	return render(request, 'homeTC.html',{'encabezado':'TC Home page'})

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Account created successfully")
			login(request,user)
			return redirect('TC home')
		else:
			messages.error(request, "Error Creating user, please follow the instructions")
			return redirect('ingreso')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form':form, 'encabezado':'Admin Sign Up'})


def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('TC home')
		else:
			message="Incorrect username or password"
			return render(request, 'login.html',{'form':AuthenticationForm,
				'encabezado':'TC login', 'message':message})
		
		
	else:
		form = AuthenticationForm()
	return render(request, 'login.html',{'form':form, "encabezado":"TC login"})
		
@login_required
def signout(request):
	logout(request)
	return redirect('TC home')


def ingresa(request):
	return render(request, 'no.html',{'encabezado':'Not today'})


def prueba(request):
	signup = UserCreationForm()
	login = AuthenticationForm()
	return render(request, 'ingreso.html',{'signup':signup, 'login':login})			