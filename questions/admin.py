from django.contrib import admin

from .models import Question, UserWithAvatar

admin.site.register(Question)
admin.site.register(UserWithAvatar)
