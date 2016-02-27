# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields
import ui.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('export_id', models.CharField(default=ui.models.default_uuid, unique=True, max_length=32)),
                ('export_type', models.CharField(max_length=255, blank=True)),
                ('export_format', models.CharField(default=b'csv', max_length=10, choices=[(b'csv', b'Comma separated values (CSV)'), (b'tsv', b'Tab separated values (TSV)'), (b'html', b'HTML'), (b'xlsx', b'Excel (XLSX)'), (b'json', b'JSON'), (b'json_full', b'Full JSON')])),
                ('status', models.CharField(default=b'requested', max_length=20, choices=[(b'requested', b'requested'), (b'completed success', b'completed success'), (b'completed failure', b'completed failure')])),
                ('path', models.TextField()),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('date_started', models.DateTimeField(null=True, blank=True)),
                ('date_ended', models.DateTimeField(null=True, blank=True)),
                ('dedupe', models.BooleanField(default=False)),
                ('item_date_start', models.DateTimeField(null=True, blank=True)),
                ('item_date_end', models.DateTimeField(null=True, blank=True)),
                ('harvest_date_start', models.DateTimeField(null=True, blank=True)),
                ('harvest_date_end', models.DateTimeField(null=True, blank=True)),
                ('infos', jsonfield.fields.JSONField(default=dict, blank=True)),
                ('warnings', jsonfield.fields.JSONField(default=dict, blank=True)),
                ('errors', jsonfield.fields.JSONField(default=dict, blank=True)),
                ('seed_set', models.ForeignKey(blank=True, to='ui.SeedSet', null=True)),
                ('seeds', models.ManyToManyField(to='ui.Seed')),
                ('user', models.ForeignKey(related_name='exports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
