# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_todos'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='done_by',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
