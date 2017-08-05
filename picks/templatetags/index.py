from django import template
register = template.Library()

@register.filter
def team_picked(sequence, position):
    return sequence[position]['team_picked']

@register.filter
def margin(sequence, position):
    return sequence[position]['margin']