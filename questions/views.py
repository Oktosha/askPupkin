from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from . import forms
from django.contrib.auth.models import User

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
			new_user = User.objects.create_user(**form.cleaned_data)
			auth_views.login(request, new_user)
			return redirect('questions:index')
	else:
		form = forms.UserForm()

	return render(request, 'registration/signup.html', {'form': form})
