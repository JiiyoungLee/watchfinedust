# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkdusts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dustinfo',
            name='dust',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationinfo',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationinfo',
            name='longtitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
