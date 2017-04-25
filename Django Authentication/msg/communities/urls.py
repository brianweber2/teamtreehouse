from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.AllCommunities.as_view(), name="list"),
    url(r"^new/$", views.CreateCommunity.as_view(), name="create"),
    url(
        r"^posts/in/(?P<slug>[-\w]+)/$",
        views.SingleCommunity.as_view(),
        name="single"
    ),
    url(
        r"join/(?P<slug>[-\w]+)/$",
        views.JoinCommunity.as_view(),
        name="join"
    ),
    url(
        r"leave/(?P<slug>[-\w]+)/$",
        views.LeaveCommunity.as_view(),
        name="leave"
    ),
    url(
        r"change_status/(?P<slug>[-\w]+)/(?P<user_id>\d+)/(?P<status>\d)/$",
        views.ChangeStatus.as_view(),
        name="change_status"
    ),
]
