# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
