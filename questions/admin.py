from django.contrib import admin

from .models import Question, UserWithAvatar, Answer

admin.site.register(Question)
admin.site.register(UserWithAvatar)
admin.site.register(Answer)
