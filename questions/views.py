from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from . import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Question
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/index.html', context)

def logout(request):
    auth_views.logout(request)
    return redirect('questions:index')

@login_required
def ask(request):
    redirect_to = 'questions:index'
    if request.method == 'POST':
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.pub_date = timezone.now()
            question.save()
            return redirect(redirect_to)
    else:
        form = forms.AskForm()
    context = {'form': form }
    return render(request, 'questions/ask.html', context)


def signup(request):
    redirect_to = request.GET.get('next', 'questions:index')
    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(redirect_to)
    else:
        form = forms.UserForm()
    context = {'form': form }
    next = request.GET.get('next', None)
    if next:
        context['next'] = next
    return render(request, 'registration/signup.html', context)
