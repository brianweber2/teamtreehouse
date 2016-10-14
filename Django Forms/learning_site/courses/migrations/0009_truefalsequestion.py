# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_multiplechoicequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, to='courses.Question', serialize=False, primary_key=True, parent_link=True)),
            ],
            bases=('courses.question',),
        ),
    ]
