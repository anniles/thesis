# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='category',
            field=models.CharField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')], default=1, max_length=2),
        ),
    ]
