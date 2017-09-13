# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qasite', '0004_artile_is_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artile',
            name='is_enable',
            field=models.BooleanField(default=True),
        ),
    ]
