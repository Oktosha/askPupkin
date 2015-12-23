from django import template
from questions.models import Answer, Tag
from django.db.models import Count

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

@register.inclusion_tag('questions/questionlist.html')
def question_list(questions):
    return { 'questions': questions}
    
@register.inclusion_tag('questions/answercard.html')
def answer_card(answer):
    return { 'answer': answer }

@register.inclusion_tag('questions/tagcloud.html')
def popular_tags():
    tags = Tag.objects.annotate(n_questions=Count('question')).order_by('n_questions').reverse()[:20]
    return { 'tags': tags }