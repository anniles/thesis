# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-30 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20170126_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='room_image')),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.AddField(
            model_name='roomimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hotels.Room'),
        ),
    ]
