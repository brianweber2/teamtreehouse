# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='courses.Question', primary_key=True, serialize=False)),
            ],
            bases=('courses.question',),
        ),
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='courses.Question', primary_key=True, serialize=False)),
            ],
            bases=('courses.question',),
        ),
    ]
