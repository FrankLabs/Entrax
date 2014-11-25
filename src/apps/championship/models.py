# -*- coding: utf-8 -*-

from django.db import models
from model_utils import Choices
from datetime import datetime

from core.models import Citie
from rider.models import ProfileRider

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


class Championship(models.Model):

    name = models.CharField('Name', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)


class Championship_Detail(models.Model):

    name = models.ForeignKey(Championship, related_name='detail')
    place = models.ForeignKey(Citie, blank=True, null=True)
    club = models.ManyToManyField(Organization_Club, blank=True, null=True,
                related_name='championship')

    date = models.Datetime('Championship date', datetime.date())

    def __unicode__(self):
        return "%s, %s" % (self.name, self.date)

    def not_equal_date(self, championship, date):
        detail = Championship_Detail.objects.filter(
                    name = championship,
                    date = date
                )
        if len(detail) != 0:
            return False
        else:
            return True


class Times(models.Model):

    rider_level = models.ForeignKey(Level, related_name='level')

    time = models.DecimalField('Times', 
                max_digits=5, decimal_places=3, default=0)


class Level(models.Model):

    rider = models.ForeignKey(ProfileRider, related_name='rider')
    championship = models.ForeignKey(Championship, related_name='championship')

    dicipline = models.PositiveIntegerField('Dicipline'),
                            choices=DICIPLINE_CHOICES, max_length=1)
    category = models.PositiveIntegerField('Category'),
                            choices=CATEGIRY_CHOICES, max_length=2)
    rider_number = models.PositiveIntegerField('Rider number'), max_length=3)
    result = models.PositiveIntegerField('Result'), max_length=2)

    def __unicode__(self):
        return "%s, %s" % (self.championship, self.rider,)

    def is_unique(self, rider, championship):
        level = Level.objects.filter(
                    rider = rider, 
                    championship = championship
                )
        if len(level) != 0:
            return False
        else:
            return True

