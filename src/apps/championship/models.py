from django.db import models

from apps.core.models import Citie
from apps.rider.models import ProfileRider
from datetime import datetime


class Club(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name,)


class ChampionshipDetail(models.Model):
    discipline = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    club_organizer = models.ForeignKey(Club, null=True, blank=True)
    location = models.ForeignKey(Citie, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name,)

    def month(self):
        return self.date.month

    def year(self):
        return self.date.year

    def set_date(self, day, month, year):
        self.date = datetime(year, month, day).date()
        self.save()


class Statistic(models.Model):
    category = models.CharField(max_length=100)
    championship = models.ForeignKey(ChampionshipDetail)
    rider = models.ForeignKey(ProfileRider)
    result = models.PositiveIntegerField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    laps = models.PositiveIntegerField(null=True, blank=True)
    dif_1 = models.TimeField(null=True, blank=True)
    dif_ante = models.TimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.category,)


class Lap(models.Model):
    number = models.PositiveInteger(null=True, blank=True)
    lap = models.TimeField(null=True, blank=True)
    statistic = models.ForeignKey(Statistic)

    def __unicode__(self):
        return "%s" % (self.number,)
