# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='mate',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='mate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mate',
            name='last_name',
            field=models.CharField(default='lastname', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mate',
            name='picture',
            field=models.CharField(default='#', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nickname',
            name='mate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Mate'),
        ),
    ]
