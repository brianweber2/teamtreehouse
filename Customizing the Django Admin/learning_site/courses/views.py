from itertools import chain

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import forms
from . import models


def course_list(request):
    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key=lambda s: s.order)
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'steps': steps
    })


def text_step(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/text_step.html', {'step': step})


def quiz_step(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/quiz_step.html', {'step': step})


@login_required
def quiz_create(request, course_pk):
    course = get_object_or_404(models.Course, pk=course_pk)
    form = forms.QuizForm()
    if request.method == 'POST':
        form = forms.QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {
        'course': course,
        'form': form
    })


@login_required
def quiz_edit(request, course_pk, quiz_pk):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk, course_id=course_pk)
    form = forms.QuizForm(instance=quiz)
    if request.method == 'POST':
        form = forms.QuizForm(instance=quiz, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(quiz.title))
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {
        'course': quiz.course,
        'form': form
    })


@login_required
def create_question(request, quiz_pk, question_type):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk)
    if question_type == 'tf':
        form_class = forms.TrueFalseQuestionForm
    else:
        form_class = forms.MultipleChoiceQuestionForm

    form = form_class()
    answer_forms = forms.AnswerInlineFormSet(
        queryset=models.Answer.objects.none()
    )

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            messages.success(request, "Added question")
            return HttpResponseRedirect(quiz.get_absolute_url())

    return render(request, 'courses/question_form.html', {
        'quiz': quiz,
        'form': form,
        'formset': answer_forms
    })


@login_required
def edit_question(request, quiz_pk, question_pk):
    question = get_object_or_404(models.Question,
                                 pk=question_pk, quiz_id=quiz_pk)
    if hasattr(question, 'truefalsequestion'):
        form_class = forms.TrueFalseQuestionForm
    else:
        form_class = forms.MultipleChoiceQuestionForm

    form = form_class(instance=question)
    answer_forms = forms.AnswerInlineFormSet(
        queryset=form.instance.answer_set.all()
    )

    if request.method == 'POST':
        form = form_class(request.POST, instance=question)
        answer_forms = forms.AnswerInlineFormSet(request.POST)
        if form.is_valid() and answer_forms.is_valid():
            form.save()
            answer_forms.save()
            messages.success(request, "Updated question")
            return HttpResponseRedirect(form.instance.get_absolute_url())

    return render(request, 'courses/question_form.html', {
        'quiz': question.quiz,
        'form': form,
        'formset': answer_forms
    })


@login_required
def answer_form(request, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk)
    form = forms.AnswerForm()

    if request.method == 'POST':
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            messages.success(request, "Added answer")
            return HttpResponseRedirect(question.quiz.get_absolute_url())
    return render(request, 'courses/answer_form.html', {'form': form})
