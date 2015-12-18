from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Question, UserWithAvatar

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    class Meta:
        model = UserWithAvatar
        fields = ("username", "email", "password1", "password2", "avatar")
    

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.avatar = self.cleaned_data["avatar"]
        if commit:
            user.save()
        return user

class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ("title", "text")