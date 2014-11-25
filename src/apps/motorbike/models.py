from django.db import models

from apps.rider.models import ProfileRider


class Motorbike(models.Model):
    rider = models.ForeignKey(ProfileRider)
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name,)
