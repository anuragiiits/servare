# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20170731_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='type',
            field=models.CharField(choices=[('song_lyrics', 'song_lyrics'), ('tongue_twister', 'tongue_twister'), ('saying', 'saying'), ('poem', 'poem'), ('story', 'story'), ('help', 'help')], max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='type',
            field=models.CharField(choices=[('song_lyrics', 'song_lyrics'), ('tongue_twister', 'tongue_twister'), ('saying', 'saying'), ('poem', 'poem'), ('story', 'story'), ('help', 'help')], max_length=50),
        ),
    ]
