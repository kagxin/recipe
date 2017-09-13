# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qasite', '0003_tag_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='artile',
            name='is_enable',
            field=models.BooleanField(default=datetime.datetime(2017, 7, 1, 9, 49, 34, 71644, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
