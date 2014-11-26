from django.db import models

from apps.core.models import Citie
from apps.rider.models import ProfileRider
from datetime import datetime

FIRST = 1


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
    total_time = models.TimeField(null=True, blank=True)
    total_laps = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.category,)

    def diff_1(self):
        winner_stats = Statistic.objects.get(championship=self.championship,
                                             result=FIRST)
        return winner_stats.total_time - self.total_time

    def diff_prev(self):
        if self.result != FIRST:
            prev_statistic = Statistic.objects.get(
                championship=self.championship,
                result=self.result - 1)
            result = prev_statistic.total_time - self.total_time
        else:
            result = datetime.min.time()
        return result


class Lap(models.Model):
    number = models.PositiveInteger(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    statistic = models.ForeignKey(Statistic)

    def __unicode__(self):
        return "%s" % (self.number,)
