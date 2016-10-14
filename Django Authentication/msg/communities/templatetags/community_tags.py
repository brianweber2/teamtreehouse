from django import template

from .. import models

register = template.Library()


@register.simple_tag
def get_all_communities():
    return models.Community.objects.all()


@register.simple_tag(takes_context=True)
def get_user_communities(context):
    return context["user"].communities.select_related("community").all()


@register.simple_tag(takes_context=True)
def get_other_communities(context):
    if context["user"].is_authenticated():
        return models.Community.objects.exclude(
            pk__in=context["user"].communities.select_related(
                "community").values_list("community")
        )
    return models.Community.objects.all()


@register.inclusion_tag("communities/_buttons.html", takes_context=True)
def community_buttons(context, community):
    user = context["user"]
    response = {"community": community, "in_community": False}
    if user in community.members.all():
        response["in_community"] = True
    return response
