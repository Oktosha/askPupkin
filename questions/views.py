from django.shortcuts import render

def index(request):
	context = {}
	return render(request, 'questions/index.html', context)