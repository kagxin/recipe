# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('qasite', '0002_auto_20170701_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='uuid',
            field=models.CharField(default=datetime.datetime(2017, 7, 1, 9, 15, 18, 580053, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
