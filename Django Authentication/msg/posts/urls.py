from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.AllPosts.as_view(), name="all"),
    url(r"new/$", views.CreatePost.as_view(), name="create"),
    url(
        r"by/(?P<username>[-\w]+)/$",
        views.UserPosts.as_view(),
        name="for_user"
    ),
    url(
        r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
        views.SinglePost.as_view(),
        name="single"
    ),
    url(
        r"delete/(?P<pk>\d+)/$",
        views.DeletePost.as_view(),
        name="delete"
    ),
]
