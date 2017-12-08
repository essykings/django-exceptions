# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
