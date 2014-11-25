# -*- coding: utf-8 -*-

from django.db import models

from apps.rider.models import ProfileRider
from apps.championship.models import Championship


class Motorbike(models.Model):

    """ Motocicletas

    Las motocicletas están asociadas a su dueño (un corredor) y al campeonato al
    que está inscripta.
    Los datos que se tienen de la moto son la marca y el modelo.
    """

    rider = models.ForeignKey(ProfileRider, related_name='motorbike')
    championship = models.ForeignKey(Championship, related_name='championship')
    bike_brand = models.CharField('Brand', max_length=200)
    bike_model = models.CharField('Model', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = 'Motorbike'
        verbose_name_plural = 'Motorbikes'

    def get_brand(self):
        return self.bike_brand

    def get_model(self):
        return self.bike_model

    """Devuelve el campeonato al que está inscripta la moto.
    """
    def get_championship(self):
        return self.championship




