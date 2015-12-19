from django.contrib import admin

from .models import Question, UserWithAvatar, Answer, Tag, Like

admin.site.register(UserWithAvatar)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Like)
