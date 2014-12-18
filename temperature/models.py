from django.db import models


# Create your models here.
class Thermocouple(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    def latest_reading(self):
        reading = (Reading.objects.filter(thermocouple=self)
                   .order_by('-date').values()[0])
        return reading

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.short_name)


class Reading(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()
    thermocouple = models.ForeignKey(Thermocouple)

    def __unicode__(self):
        return '%s - %sc' % (self.date, self.value)
