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
    championship = models.ForeignKey(Championship, related_name='championship')

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

    def is_unique(self, rider, championship):
        level = Level.objects.filter(
                    rider = rider, 
                    championship = championship
                )
        if len(level) != 0:
            return False
        else:
            return True

    def get_times(self):
        if self.times.exists():
            return self.times.time

    def total_time(self):
        times = self.get_times()
        time = 0
        for elem in times:
            time = time + elem
        return time

    def difference(self, level):
        my_time = self.total_time()
        level_time = level.total_time()
        time = abs(my_time - level_time)
        return time


class Times(models.Model):

    rider_level = models.ForeignKey(Level, related_name='times')

    time = models.DecimalField(
                'Times', 
                max_digits=5, 
                decimal_places=3
            )

    class Meta:
        verbose_name        = 'Times'
        verbose_name_plural = 'Times'
    """
    Otra alternativa es hacer el min_value en el form pero no es lindo

    time = models.DecimalField(
                'Times', 
                max_digits=5, 
                decimal_places=3, 
                min_value = 0.01
            )

    from decimal import Decimal
    time = forms.DecimalField(min_value = decimal.Decimal("0.01"))
    """