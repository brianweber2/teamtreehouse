from django import template

from .. import forms

register = template.Library()


@register.inclusion_tag("posts/_modal.html", takes_context=True)
def post_form(context):
    form = forms.PostForm(user=context["user"])
    return {"form": form}
