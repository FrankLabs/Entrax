# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

from apps.core.models import Citie
from apps.rider.models import ProfileRider


class Discipline(models.Model):

    name = models.CharField('Disciplina', max_length=100)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'


class Category(models.Model):

    name = models.CharField('Categoría', max_length=100)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Organizing_Club(models.Model):

    name = models.CharField('Organizing Club', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = 'Club Organizador'
        verbose_name_plural = 'Club Organizador'


class Championship(models.Model):

    name = models.CharField('Name', max_length=200)
    place = models.ForeignKey(Citie, blank=True, null=True)
    date = models.DateTimeField('Championship date', blank=True, null=True)
    club = models.ManyToManyField(
        Organizing_Club,
        blank=True,
        null=True,
        related_name='organizing_club'
    )
    riders = models.ManyToManyField(
        ProfileRider,
        null=True,
        related_name='rider'
    )

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'

    def not_equal_date(self, championship, date):
        detail = Championship.objects.filter(
                    name = championship,
                    date = date
                )
        return len(detail) == 0

