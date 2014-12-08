# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0003_auto_20141201_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 13, 47, 36, 783400), verbose_name=b'Create date'),
            preserve_default=True,
        ),
    ]
