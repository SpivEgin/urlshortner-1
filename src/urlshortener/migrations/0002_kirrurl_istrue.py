# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-14 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='istrue',
            field=models.BinaryField(default=True),
        ),
    ]
