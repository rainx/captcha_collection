# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaAnwser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=30)),
                ('img_content', models.BinaryField()),
                ('anwser', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
