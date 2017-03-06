# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_mate_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mate',
            name='first_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='mate',
            name='last_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='mate',
            name='picture',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
