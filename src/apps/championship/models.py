from django.db import models

from apps.core.models import Citie
from apps.rider.models import ProfileRider


class Discipline(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s" % (self.name,)


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s" % (self.name,)


class Race(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField(null=True, blank=True)
	citie = models.ForeignKey(Citie)
	category = models.ForeignKey(Category)
	discipline = models.ForeignKey(Discipline)
	laps = models.PositiveSmallIntegerField(null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.name,)

	def get_full_name(self):		
		return "%s, %s, %s, %s, categoria %s" % (self.name, self.date, self.discipline, self.category)

	@property
	def year(self):
		return "%s" % (self.date.year)


class LapTime(models.Model):
	race = models.ForeignKey(Race)
	rider = models.ForeignKey(ProfileRider, null=False, blank=False)
	lap_number = models.PositiveSmallIntegerField(null=False, blank=False)
	time = models.TimeField()


class RaceResult(models.Model):
	race = models.ForeignKey(Race)
	rider = models.ForeignKey(ProfileRider)
	position = models.PositiveSmallIntegerField(null=False, blank=False)
	completed_laps = models.PositiveSmallIntegerField(null=False, blank=False)
	finished = models.BooleanField(null=False, blank=False)
	total_time = models.TimeField(null=True, blank=True)
	points = models.PositiveSmallIntegerField(null=True, blank=True)


class Championship(models.Model):
	name = models.CharField(max_length=100)
	discipline = models.ForeignKey(Discipline)
	category = models.ForeignKey(Category)
	year = models.date.year(null=True, blank=True)
	finished = models.BooleanField(null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.name,)



