# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151219_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False),
        ),
    ]
