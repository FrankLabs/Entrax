# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='championshipinscription',
            name='penal_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='championship',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 29, 13, 28, 57, 850434), verbose_name=b'Create date'),
            preserve_default=True,
        ),
    ]
