# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-22 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='academicSubject',
            new_name='academicsubject',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bookType',
            new_name='booktype',
        ),
    ]