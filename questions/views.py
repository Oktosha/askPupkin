from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

def index(request):
	context = {}
	return render(request, 'questions/index.html', context)

def logout(request):
	auth_views.logout(request)
	return redirect('questions:index')