# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0002_auto_20141129_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 6, 15, 53, 39, 27710), verbose_name=b'Create date'),
            preserve_default=True,
        ),
    ]
