# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
        ('word', '0007_auto_20170806_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalword',
            name='language',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='language.Language'),
        ),
        migrations.AddField(
            model_name='word',
            name='language',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='words', to='language.Language'),
            preserve_default=False,
        ),
    ]
