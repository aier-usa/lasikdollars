# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20160907_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='website',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
