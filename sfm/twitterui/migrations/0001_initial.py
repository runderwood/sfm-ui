# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterSeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.TextField(blank=True)),
                ('uid', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('stats', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('twitter_extra_field', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
