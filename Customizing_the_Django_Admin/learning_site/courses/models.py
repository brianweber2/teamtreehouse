from django.core.urlresolvers import reverse
from django.db import models

import math

STATUS_CHOICES = (
    ('i', 'In Progress'),
    ('r', 'In Review'),
    ('p', 'Published'),
)


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_live = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i')
    
    def __str__(self):
        return self.title
    
    def time_to_complete(self):
        from courses.templatetags.course_extras import time_estimate
        return '{} min.'.format(time_estimate(len(self.description.split())))

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title


class Text(Step):
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('courses:text_step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.pk
        })


class Quiz(Step):
    total_questions = models.IntegerField()

    class Meta:
        verbose_name_plural = "quizzes"

    def get_absolute_url(self):
        return reverse('courses:quiz_step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.pk
        })
    
    def number_correct_needed(self):
        return '{}/{}'.format(math.ceil(self.total_questions * 0.7), self.total_questions)



class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order',]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt


class MultipleChoiceQuestion(Question):
    shuffle_answers = models.BooleanField(default=False)


class TrueFalseQuestion(Question):
    pass


class Answer(models.Model):
    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text