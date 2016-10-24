# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20151124_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('order', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(to='courses.Question')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
