from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from . import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Question, Answer, UserWithAvatar
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/index.html', context)

def logout(request):
    auth_views.logout(request)
    return redirect('questions:index')

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    context = {'question': question, 'answers': answers }
    return render(request, 'questions/question.html', context)

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

def user(request, user_id):
    user = get_object_or_404(UserWithAvatar, pk=user_id)
    n_questions = Question.objects.filter(author=user).count()
    n_answers = Answer.objects.filter(author=user).count()
    context = {"user": user, "n_questions": n_questions, "n_answers": n_answers}
    return render(request, 'questions/user.html', context)
