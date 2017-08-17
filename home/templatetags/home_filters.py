from django import template
import pdb
register = template.Library()

@register.filter
def users_pick(sequence, position):
    return sequence[position].team_picked

@register.filter
def users_margin(sequence, position):
    return sequence[position].margin