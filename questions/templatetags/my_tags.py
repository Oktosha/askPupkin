from django import template
from questions.models import Answer, Tag

register = template.Library()

@register.inclusion_tag('questions/inputfield.html')
def input_field(field, label):
    return { 'field': field, 'label': label }

@register.inclusion_tag('questions/questioncard.html')
def question_card(question):
    n_likes = question.likes.count()
    n_answers = Answer.objects.filter(question=question).count()
    tags = Tag.objects.filter(question=question)
    return { 'question': question, 'n_likes':n_likes, 'n_answers': n_answers, 'tags': tags }

@register.inclusion_tag('questions/answercard.html')
def answer_card(answer):
    return { 'answer': answer }