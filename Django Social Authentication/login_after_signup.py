from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from . import forms


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy("products:list")
    
    def form_valid(self, form):
        res = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return res
        
                              