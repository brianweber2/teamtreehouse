from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView


#def home(request):
#    return render(request, 'home.html')


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games_today"] = 6
        return context


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World!")