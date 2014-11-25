from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name,)


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name,)


class Citie(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name,)

    @property
    def country(self):
        try:
            return self.state.country
        except:
            return None

    def get_location(self):
        return "%s, %s, %s" % (self.name, self.state, self.country)
