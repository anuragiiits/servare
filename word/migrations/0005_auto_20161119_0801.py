# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-19 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0004_auto_20161013_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='word',
            name='translations',
        ),
        migrations.AddField(
            model_name='translation',
            name='bavarian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bavarian', to='word.Word'),
        ),
        migrations.AddField(
            model_name='translation',
            name='desc',
            field=models.ManyToManyField(blank=True, to='word.Description'),
        ),
        migrations.AddField(
            model_name='translation',
            name='foreign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreign', to='word.Word'),
        ),
    ]