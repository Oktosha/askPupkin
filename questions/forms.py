from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Question, UserWithAvatar

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = UserWithAvatar
        fields = ("username", "email", "password1", "password2")
    

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ("title", "text")