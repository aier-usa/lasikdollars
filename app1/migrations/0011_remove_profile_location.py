# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20170504_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
