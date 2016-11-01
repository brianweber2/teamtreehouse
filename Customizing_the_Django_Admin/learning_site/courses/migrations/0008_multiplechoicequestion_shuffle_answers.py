# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_multiplechoicequestion_truefalsequestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='shuffle_answers',
            field=models.BooleanField(default=False),
        ),
    ]
