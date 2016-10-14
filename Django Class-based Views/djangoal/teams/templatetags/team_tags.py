import random

from django import template

register = template.Library()


@register.inclusion_tag('teams/_team.html')
def team_avatar(team):
    return {'team': team, 'num': random.randint(0, 215)}
