# -*- coding: utf-8 -*-

from django.db import models

from rider.models import ProfileRider

# Create your models here.
class Motorbike_Brand(models.Model):

	name = models.CharField('Brand', max_length=200)

	def __unicode__(self):
        return "%s" % (self.name,)


class Motorbike_Model(models.Model):

	brand = models.ForeignKey(Motorbike_Brand, related_name='motorbike')

	name = models.CharField('Model', max_length=200)

	def __unicode__(self):
        return "%s, %s" % (self.brand, self.name,)


class Motorbike(models.Model):

	rider = models.ForeignKey(ProfileRider, related_name='motorbike')
	model = models.ForeignKey(Motorbike_Model)

	def __unicode__(self):
        return "%s, %s" % (self.rider, self.model,)