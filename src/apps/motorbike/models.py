# -*- coding: utf-8 -*-

from django.db import models

from apps.rider.models import ProfileRider
from apps.championship.models import Championship


class Motorbike_Brand(models.Model):

    """ Marcas de motocicletas.
    """
    name = models.CharField('Brand', max_length=200)

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = 'Marca de motocicleta'
        verbose_name_plural = 'Marcas de motocicletas'


class Motorbike_Model(models.Model):

    """ Modelos de motocicletas.
    """

    name = models.CharField('Model', max_length=200)
    bike_brand = models.ForeignKey(
        Motorbike_Brand,
        related_name='motorbike_brand',
        null=True,
    )

    def __unicode__(self):
        return "%s, %s" % (self.get_brand(), self.name,)

    class Meta:
        verbose_name = 'Modelo de motocicleta'
        verbose_name_plural = 'Modelos de motocicletas'

    def get_brand(self):
        try:
            return bike_brand.name
        except:
            return ''


class Motorbike(models.Model):

    """ Motocicletas

    Las motocicletas están asociadas a su dueño (un corredor) y al campeonato
    al que está inscripta.
    Los datos que se tienen de la moto son la marca y el modelo.
    """

    rider = models.ForeignKey(ProfileRider, related_name='motorbike')
    championship = models.ManyToManyField(
        Championship,
        related_name='championship'
    )
    bike_model = models.ForeignKey(
        Motorbike_Model,
        related_name='motorbike_model'
    )

    class Meta:
        verbose_name = 'Motocicleta'
        verbose_name_plural = 'Motocicletas'

    def __unicode__(self):
        return "%s, %s, %s" % (self.rider, self.bike_model, self.bike_brand)

    def get_brand(self):
        return self.bike_model.get_brand()

    def get_model(self):
        return self.bike_model

    """ Devuelve el campeonato al que está inscripta la moto.
    """
    def get_championship(self):
        return self.championship
