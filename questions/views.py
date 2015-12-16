from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

def index(request):
	context = {}
	return render(request, 'questions/index.html', context)

def logout(request):
	auth_views.logout(request)
	return redirect('questions:index')

def signup(request):
	if request.method == 'POST':
		form = forms.UserForm(request.POST)
		if form.is_valid():
			form.save()
			user = authenticate(username=form.cleaned_data['username'],
								password=form.cleaned_data['password1'])
			login(request, user)
			return redirect('questions:index')
	else:
		form = forms.UserForm()

	return render(request, 'registration/signup.html', {'form': form})
