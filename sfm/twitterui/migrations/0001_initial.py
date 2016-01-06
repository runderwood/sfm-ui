# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterFilterSeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('stats', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('track', models.TextField(blank=True)),
                ('follow', models.TextField(blank=True)),
                ('location', models.TextField(blank=True)),
                ('seed_set', models.ForeignKey(related_name='+', to='ui.SeedSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterSearchSeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('stats', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('query', models.TextField()),
                ('seed_set', models.ForeignKey(related_name='+', to='ui.SeedSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterUserSeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('stats', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('screen_name', models.TextField()),
                ('seed_set', models.ForeignKey(related_name='+', to='ui.SeedSet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
