# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_export'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='date_requested',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='export',
            name='export_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='export',
            name='path',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='export',
            name='seeds',
            field=models.ManyToManyField(to='ui.Seed', blank=True),
        ),
    ]
