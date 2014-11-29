# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0002_auto_20141123_1426'),
        ('motorbike', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discipline', models.IntegerField(blank=True, null=True, verbose_name=b'Discipline', choices=[(1, b'Enduro'), (2, b'Cross')])),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('description', models.TextField(max_length=3000, verbose_name=b'Description')),
                ('start_date', models.DateTimeField(null=True, verbose_name=b'Start championship date', blank=True)),
                ('finish_date', models.DateTimeField(null=True, verbose_name=b'Finish championship date', blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2014, 11, 29, 13, 22, 23, 64228), verbose_name=b'Create date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=b'Modified date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChampionshipCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_laps', models.PositiveIntegerField(default=0, max_length=3)),
                ('categoty', models.ForeignKey(to='championship.Category')),
                ('championship', models.ForeignKey(to='championship.Championship')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChampionshipInscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(default=0, max_length=3)),
                ('position', models.PositiveIntegerField(default=0, max_length=3)),
                ('total_time', models.TimeField(null=True, blank=True)),
                ('dif_time', models.TimeField(null=True, blank=True)),
                ('championship', models.ForeignKey(to='championship.ChampionshipCategory')),
                ('motorobike', models.ForeignKey(blank=True, to='motorbike.Motorbike', null=True)),
                ('rider', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(blank=True, to='rider.Team', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InscriptionLaps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_lap', models.PositiveIntegerField(default=0, max_length=3)),
                ('time', models.TimeField(null=True, blank=True)),
                ('inscription', models.ForeignKey(to='championship.ChampionshipInscription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='championship',
            name='organizer',
            field=models.ManyToManyField(to='championship.Organizer', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='championship',
            name='place',
            field=models.ForeignKey(blank=True, to='core.Citie', null=True),
            preserve_default=True,
        ),
    ]
