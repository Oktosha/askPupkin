from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import Question, UserWithAvatar, Tag

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
    tags = forms.CharField(required=False, 
        validators=[RegexValidator("^[0-9a-z]+([\s]+[0-9a-z]+)*$")])
    class Meta:
        model = Question
        fields = ("title", "text")

    def save_tags(self, question):
        tagList = map(str.strip, self.cleaned_data["tags"].split())
        for tagname in tagList:
            tag, is_created = Tag.objects.get_or_create(name=tagname)
            tag.save()
            question.tags.add(tag)
        question.save()