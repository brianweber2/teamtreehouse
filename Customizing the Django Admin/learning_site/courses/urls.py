from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_step,
        name='text_step'),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$', views.quiz_step,
        name='quiz_step'),
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create,
        name='create_quiz'),
    url(r'(?P<course_pk>\d+)/edit_quiz/(?P<quiz_pk>\d+)/$', views.quiz_edit,
        name='edit_quiz'),
    url(r'(?P<quiz_pk>\d+)/create_question/(?P<question_type>mc|tf)/$',
        views.create_question, name='create_question'),
    url(r'(?P<quiz_pk>\d+)/edit_question/(?P<question_pk>\d+)/$',
        views.edit_question, name='edit_question'),
    url(r'(?P<question_pk>\d+)/add_answer/$',
        views.answer_form, name='add_answer'),
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]