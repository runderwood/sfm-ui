# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
        ('twitterui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterseed',
            name='seed_set',
            field=models.ForeignKey(related_name='seeds', to='ui.SeedSet'),
        ),
    ]
