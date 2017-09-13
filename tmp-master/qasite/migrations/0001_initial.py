# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('context', models.TextField()),
                ('picture', models.CharField(max_length=500)),
                ('uuid', models.CharField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')),
                ('create_user', models.ForeignKey(help_text='创建用户', verbose_name='创建用户', to=settings.AUTH_USER_MODEL, related_name='creater')),
            ],
        ),
        migrations.CreateModel(
            name='commets',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('context', models.TextField()),
                ('uuid', models.CharField(max_length=500)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')),
                ('artile', models.ForeignKey(to='qasite.Artile', related_name='commets')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tag', models.CharField(max_length=50)),
                ('artile', models.ForeignKey(to='qasite.Artile', related_name='tags')),
            ],
        ),
    ]
