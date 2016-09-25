from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import mixins
from . import models


#def team_list(request):
#    teams = models.Team.objects.all()
#    return render(request, 'teams/team_list.html', {'teams': teams})
#
#
#def team_detail(request, pk):
#    team = get_object_or_404(models.Team, pk=pk)
#    return render(request, 'teams/team_detail.html', {'team': team})


class TeamListView(CreateView, ListView):
    fields = ("name", "practice_location", "coach")
    context_object_name = "teams"
    model = models.Team
    template_name = "teams/team_list.html"
    
    
class TeamDetailView(DetailView, UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    template_name = "teams/team_detail.html"
    
    
class TeamCreateView(LoginRequiredMixin, mixins.PageTitleMixin, mixins.SuccessMessageMixin, CreateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    page_title = "Create a new team"
    success_message = "Team was created successfully!"
    
    def get_inital(self):
        initial = super().get_initial()
        initial["coach"] = self.request.user.pk
        return initial
    
    
class TeamUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, mixins.SuccessMessageMixin, UpdateView):
    fields = ("name", "practice_location", "coach")
    model = models.Team
    
    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.name)
    
    def get_success_message(self):
        obj = self.get_object()
        return "{} was successfully updated!".format(obj.name)
    
    
class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Team
    success_url = reverse_lazy("teams:list")
    
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(coach=self.request.user)
        return self.model.objects.all()