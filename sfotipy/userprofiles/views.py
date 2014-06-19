from django.shortcuts import render
from .forms import UserCreationEmailForm,EmailAuthForm
from django.contrib.auth import login

def signup(request):
	form=UserCreationEmailForm(request.POST or None)
	if form.is_valid():
		form.save() 
		#loguear
		#crear Userprofiles
	return render(request,'signup.html',{'form':form})

def signin(request):
	formin=EmailAuthForm(request.POST or None)

	if formin.is_valid():
		login(request,formin.get_user())
		#redireccionar al home

	return render(request,'signin.html',{'form':formin})
