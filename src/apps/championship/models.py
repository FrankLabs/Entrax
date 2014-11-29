# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.core.models import Citie
from apps.rider.models import Team
from apps.motorobike.models import Motorbike


DISCIPLINE_CHOICES = (
    (1, 'Enduro'),
    (2, 'asd'),
)


class Organizer(models.Model):
    name = models.CharField('Name', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)


class Category(models.Model):
    name = models.CharField('Name', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)


class Championship(models.Model):
    discipline = models.IntegerField(
        'Discipline', choices=DISCIPLINE_CHOICES, blank=True, null=True
    )
    name = models.CharField('Name', max_length=200)
    description = models.TextField('Description', max_length=3000)
    place = models.ForeignKey(Citie, blank=True, null=True)
    organizer = models.ManyToManyField(
        Organizer, blank=True, null=True,
    )
    start_date = models.DateTimeField(
        'Start championship date', blank=True, null=True
    )
    finish_date = models.DateTimeField(
        'Finish championship date', blank=True, null=True
    )
    create_date = models.DateTimeField('Create date', default=datetime.now())
    modified_date = models.DateTimeField('Modified date', auto_now=True)

    def __unicode__(self):
        return "%s" % (self.name,)

    def get_category(self):
        return ChampionshipCategory.objects.filter(championship=self)


class ChampionshipCategory(models.Model):
    championship = models.ForeignKey(Championship)
    categoty = models.ForeignKey(Category)
    number_laps = models.PositiveIntegerField(max_length=3, default=0)

    def __unicode__(self):
        return "%s - %s" % (self.championship, self.categoty)

    def get_inscription(self):
        return ChampionshipInscription.objects.filter(championship=self)


class ChampionshipInscription(models.Model):
    championship = models.ForeignKey(ChampionshipCategory)
    number = models.PositiveIntegerField(max_length=3, default=0)
    position = models.PositiveIntegerField(max_length=3, default=0)
    rider = models.ForeignKey(User)
    motorobike = models.ForeignKey(Motorbike, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    total_time = models.TimeField(null=True, blank=True)
    dif_time = models.TimeField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.championship, self.rider)

    def get_total_laps(self):
        return InscriptionLaps.objects.filter(inscription=self)


class InscriptionLaps(models.Model):
    inscription = models.ForeignKey(ChampionshipInscription)
    number_lap = models.PositiveIntegerField(max_length=3, default=0)
    time = models.TimeField(null=True, blank=True)

    def __unicode__(self):
        return "%s - Lap: %s" % (self.inscription, self.number_lap)
