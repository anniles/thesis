# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-23 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20170123_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]