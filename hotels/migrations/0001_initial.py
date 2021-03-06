# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('category', models.SmallIntegerField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')], default=1)),
                ('description', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_guest', models.PositiveSmallIntegerField()),
                ('category', models.CharField(choices=[('single', 'Single'), ('double', 'Double')], default='single', max_length=200)),
                ('description', models.TextField(default='', null=True)),
                ('amenities', models.ManyToManyField(to='hotels.Amenity')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.CharField(choices=[('RO', 'Room only'), ('BB', 'Bed & Breakfast'), ('HB', 'Half Board (Breakfast and Dinner)'), ('FB', 'Full Board (Beakfast, Lunch and Dinner)'), ('AI', 'All Inclusive')], default='RO', max_length=2)),
                ('coefficient', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='roomtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.RoomType'),
        ),
    ]
