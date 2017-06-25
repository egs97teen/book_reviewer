# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0003_user_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='belt_app.User'),
        ),
    ]