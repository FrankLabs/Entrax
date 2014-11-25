# -*- coding: utf-8 -*-

from django.db import models

from apps.rider.models import ProfileRider

# Create your models here.
class Motorbike_Brand(models.Model):

    name = models.CharField('Brand', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name        = 'Motorbike Brand'
        verbose_name_plural = 'Motorbike Brands'


class Motorbike_Model(models.Model):

    brand = models.ForeignKey(Motorbike_Brand, related_name='motorbike')

    name = models.CharField('Model', max_length=200)

    def __unicode__(self):
        return "%s, %s" % (self.brand, self.name,)

    class Meta:
        verbose_name        = 'Motorbike Model'
        verbose_name_plural = 'Motorbike Models'


class Motorbike(models.Model):

    rider = models.ForeignKey(ProfileRider, related_name='motorbike')
    model = models.ForeignKey(Motorbike_Model)

    def __unicode__(self):
        return "%s, %s" % (self.rider, self.model,)

    class Meta:
        verbose_name        = 'Motorbike'
        verbose_name_plural = 'Motorbikes'