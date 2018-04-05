# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinishedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('ean_code', models.CharField(default=0, max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='SemiFinishedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.FloatField()),
                ('producer', models.CharField(max_length=255)),
            ],
        ),
    ]
