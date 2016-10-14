from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "community")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["community"].queryset = (
                models.Community.objects.filter(
                    pk__in=user.communities.values_list("community__pk")
                )
            )
