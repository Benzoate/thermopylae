import datetime
from django.core.management.base import BaseCommand, CommandError
from temperature import views
from temperature import models


class Command(BaseCommand):
    help = 'Decimates data older than 7 days'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        therms = models.Thermocouple.objects.all()
        for therm in therms:
            current = datetime.date.today() - datetime.timedelta(days=7)
            readings = list(models.Reading.objects.filter(date__lt=current,
                                                          thermocouple=therm)
                            .order_by('-date').all())
            while readings:
                todays = [i for i in readings if i.date.date() == current]
                if not todays:
                    current = current - datetime.timedelta(days=1)
                    continue
                values = map(lambda x: x.value, todays)
                print 'collating %s values' % (len(values),)

                col = models.CollatedReading()
                col.max = max(values)
                col.min = min(values)
                col.mean = sum(values) / len(values)
                col.date = current
                col.thermocouple = therm
                col.save()

                print 'min: %s, max: %s, mean: %s' % (col.min, col.max,
                                                      col.mean)

                readings = [i for i in readings if i not in todays]
                for r in todays:
                    r.delete()

                current = current - datetime.timedelta(days=1)
