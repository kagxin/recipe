# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qasite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
                ('uuid', models.CharField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')),
            ],
        ),
        migrations.RemoveField(
            model_name='commets',
            name='artile',
        ),
        migrations.AddField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ', default=datetime.datetime(2017, 7, 1, 7, 23, 30, 705682, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artile',
            name='create_user',
            field=models.ForeignKey(help_text='创建用户', verbose_name='创建用户', to=settings.AUTH_USER_MODEL, related_name='artiles'),
        ),
        migrations.DeleteModel(
            name='commets',
        ),
        migrations.AddField(
            model_name='commet',
            name='artile',
            field=models.ForeignKey(related_name='commets', to='qasite.Artile'),
        ),
        migrations.AddField(
            model_name='commet',
            name='create_user',
            field=models.ForeignKey(help_text='创建用户', verbose_name='创建用户', to=settings.AUTH_USER_MODEL, related_name='commets'),
        ),
    ]
