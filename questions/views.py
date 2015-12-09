from django.shortcuts import render
from django.contrib.auth import views as auth_views

def index(request):
	context = {}
	return render(request, 'questions/index.html', context)
