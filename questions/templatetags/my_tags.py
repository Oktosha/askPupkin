from django import template

register = template.Library()

@register.inclusion_tag('questions/inputfield.html')
def input_field(field, label):
    return { 'field': field, 'label': label }

@register.inclusion_tag('questions/questioncard.html')
def question_card(question):
    return { 'question': question }