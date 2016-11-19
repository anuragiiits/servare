# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-19 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0005_auto_20161119_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='translations',
            field=models.ManyToManyField(blank=True, related_name='_word_translations_+', through='word.Translation', to='word.Word'),
        ),
    ]
