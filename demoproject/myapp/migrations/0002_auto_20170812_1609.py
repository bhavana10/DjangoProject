# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='age',
            new_name='my_age',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='my_name',
        ),
    ]