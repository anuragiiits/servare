# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170731_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='place',
            field=models.CharField(default='Baar-Ebenhausen', max_length=150),
            preserve_default=False,
        ),
    ]