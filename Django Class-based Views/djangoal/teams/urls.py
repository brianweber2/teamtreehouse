from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TeamListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.TeamDetailView.as_view(), name='detail'),
    url(r'^create/$', views.TeamCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.TeamUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.TeamDeleteView.as_view(), name='delete'),
]
