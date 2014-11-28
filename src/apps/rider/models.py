from django.db import models
from django.contrib.auth.models import User

from apps.core.models import Citie


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name,)


class ProfileRider(models.Model):
    user = models.ForeignKey(User)
    birthday = models.DateField(null=True, blank=True)
    location = models.ForeignKey(Citie, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.user.get_full_name(),)
