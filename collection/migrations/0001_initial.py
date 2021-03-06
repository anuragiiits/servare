# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('kind', models.CharField(choices=[('song', 'liad'), ('tongue_twister', 'zunga breha'), ('saying', 'šbruh'), ('poem', 'gedihd')], max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_items', to='user.Profile')),
            ],
        ),
    ]
