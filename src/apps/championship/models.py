# -*- coding: utf-8 -*-

from django.db import models
from model_utils import Choices
from datetime import datetime

from apps.core.models import Citie
from apps.rider.models import ProfileRider

DICIPLINE_CHOICES = Choices(
            (1, 'enduro', 'Enduro'),
            (2, 'mx', 'MX'),
            (3, 'rally', 'Rally'),
            (4, 'sheet3', 'Sheet3')
            )

CATEGIRY_CHOICES = Choices(
            (1, 'junior_libre', 'Junior Libre'),
            (2, 'junior_limitada', 'Junior Limitada'),
            (3, 'promocionales', 'Promocionales'),
            (4, 'principiantes', 'Participantes'),
            (5, 'senior', 'Senior'),
            (6, 'mini_a', 'Mini A'),
            (7, 'mini_b', 'Mini B'),
            (8, 'master_a', 'Master A'),
            (9, 'master_b', 'Master B'),
            (10, 'cuatri_junior', 'Cuatri Junior'),
            (11, 'cuatri_promo', 'Cuatri Promo'),
            (12, 'cuatri_senior', 'Cuatri Senior')
            )

# Create your models here.
class Organization_Club(models.Model):

    name = models.CharField('Organization Club', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name        = 'Organization Club'
        verbose_name_plural = 'Organization Clubs'


class Championship(models.Model):

    name = models.CharField('Name', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name        = 'Championship'
        verbose_name_plural = 'Championships'


class Championship_Detail(models.Model):

    name = models.ForeignKey(Championship, related_name='detail')
    place = models.ForeignKey(Citie, blank=True, null=True)
    club = models.ManyToManyField(Organization_Club, blank=True, null=True,
                related_name='championship')

    date = models.DateTimeField('Championship date', blank=True, null=True)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.date)

    class Meta:
        verbose_name        = 'Championship Detail'
        verbose_name_plural = 'Championship Details'

    def not_equal_date(self, championship, date):
        detail = Championship_Detail.objects.filter(
                    name = championship,
                    date = date
                )
        if len(detail) != 0:
            return False
        else:
            return True


class Level(models.Model):

    rider = models.ForeignKey(ProfileRider, related_name='rider')
    championship = models.ForeignKey(
                        Championship_Detail, 
                        related_name='championship'
                    )

    dicipline = models.PositiveIntegerField('Dicipline',
                    choices=DICIPLINE_CHOICES, max_length=1)
    category = models.PositiveIntegerField('Category',
                    choices=CATEGIRY_CHOICES, max_length=2)
    rider_number = models.PositiveIntegerField('Rider number', max_length=3)
    result = models.PositiveIntegerField('Result', max_length=2)
    comment = models.TextField('Comment', blank=True)

    def __unicode__(self):
        return "%s, %s" % (self.championship, self.rider,)

    class Meta:
        verbose_name        = 'Level'
        verbose_name_plural = 'Levels'

    def is_unique(self, championship, dicipline, category, rider_number):
        level = Level.objects.filter(
                    championship = championship,
                    dicipline = dicipline, 
                    category = category,
                    rider_number = rider_number
                )
        if len(level) == 0:
            return True
        else:
            return False

    def get_times(self):
        if self.times.exists():
            return self.times.time

    def total_time(self):
        times = self.get_times()
        hour = 0
        minute = 0
        second = 0
        microsecond = 0
        for elem in times:
            hour = hour + elem.hour
            minute = minute + elem.minute
            second = second + elem.second
            microsecond = microsecond + elem.microsecond
        return datetime.time(hour, minute, second, microsecond)

    def difference(self, other):
        my_time = self.total_time()
        other_time = other.total_time()

        t1_ms = (my_time.hour*3600 + my_time.minute*60 + my_time.second)*1000\
                    + my_time.microsecond
        t2_ms = (other_time.hour*3600 + other_time.minute*60 + \
                    other_time.second)*1000 + other_time.microsecond
        time = abs(t1_ms - t2_ms)

        hour = time / (3600*1000)
        time = time % (3600*1000)

        minute = time / (60*1000)
        time = time % (60*1000)

        second = time / 1000
        time = time % 1000

        microsecond = time
        return datetime.time(hour, minute, second, microsecond)


class Times(models.Model):

    rider_level = models.ForeignKey(Level, related_name='times')

    time = models.TimeField('Times', null=True, blank=True)

    class Meta:
        verbose_name        = 'Times'
        verbose_name_plural = 'Times'