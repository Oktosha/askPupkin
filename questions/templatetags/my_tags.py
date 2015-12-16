from django import template

register = template.Library()

@register.inclusion_tag('questions/inputfield.html')
def input_field(field, label):
    return { 'field': field, 'label': label }