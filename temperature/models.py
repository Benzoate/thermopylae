from django.db import models


# Create your models here.
class Thermocouple(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    def latest_reading(self):
        reading = (Reading.objects.filter(thermocouple=self)
                   .order_by('-date').values()[0])
        return reading

    def day_min(self):
        values = (Reading.objects.filter(thermocouple=self)
                  .values_list('value', flat=True))
        # values = [item for sublist in values for item in sublist]
        return min(values)

    def day_max(self):
        values = (Reading.objects.filter(thermocouple=self)
                  .values_list('value', flat=True))
        # values = [item for sublist in values for item in sublist]
        return max(values)

    def day_mean(self):
        return 15

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.short_name)


class Reading(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()
    thermocouple = models.ForeignKey(Thermocouple)

    def __unicode__(self):
        return '%s - %sc' % (self.date, self.value)


class CollatedReading(models.Model):
    date = models.DateField()
    thermocouple = models.ForeignKey(Thermocouple)
    min = models.FloatField()
    max = models.FloatField()
    mean = models.FloatField()
