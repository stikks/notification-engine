# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import rest.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientApplication',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50)),
                ('server_key', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PushMessage',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_id', models.TextField()),
                ('target', models.TextField()),
                ('notification', rest.models.JSONField(blank=True)),
                ('body', rest.models.JSONField(blank=True)),
                ('time_to_live', models.BigIntegerField(blank=True)),
                ('priority', models.CharField(default=b'normal', max_length=6)),
                ('delay_while_idle', models.BooleanField(default=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.ClientApplication')),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_id', models.TextField()),
                ('client_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.ClientApplication')),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
    ]
