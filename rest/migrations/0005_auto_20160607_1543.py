# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20160607_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientapplication',
            options={'ordering': ('date_created',)},
        ),
        migrations.AlterModelOptions(
            name='pushmessage',
            options={'ordering': ('date_created',)},
        ),
        migrations.AddField(
            model_name='clientapplication',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 7, 15, 43, 12, 629438)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientapplication',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 7, 15, 43, 23, 409206)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 7, 15, 43, 37, 942378)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 7, 15, 43, 41, 74530)),
            preserve_default=False,
        ),
    ]
