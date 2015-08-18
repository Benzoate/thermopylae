from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import datetime

from temperature import models


def view_all(request):
    sensors = models.Thermocouple.objects.order_by('name').all()
    sensor_readings = map(lambda x: {'sensor': x,
                                     'reading': x.latest_reading(),
                                     'mean': x.day_mean(),
                                     'max': x.day_max(),
                                     'min': x.day_min(),
                                     'angle': 12}, sensors)
    blue_opacity = (min(max(14, sensor_readings[0]['reading']['value']), 22) - 14) / 8.0
    context_dict = {
        'sensor_readings': sensor_readings,
        'blue_opacity': blue_opacity
    }
    return render(request, 'temperature_index.html', context_dict)


def update_temperatures():
    sensors = models.Thermocouple.objects.values()
    r = requests.get('http://aaronlockton.com/xrf.txt')
    lines = r.text.split('\n')
    num_new_readings = 0
    for line in lines:
        try:
            date, number, end = line.split(' ')
        except ValueError:
            continue
        for sensor in sensors:
            if not end.startswith(sensor['short_name']):
                continue
            year, month, day, hour, minute, second = map(lambda x: int(x),
                                                         date.split('-'))
            ndate = datetime.datetime(year=year, month=month,
                                      day=day,
                                      hour=hour, minute=minute, second=second)
            try:
                models.Reading.objects.get(date=ndate,
                                           thermocouple_id=sensor['id'])
            except models.Reading.DoesNotExist:
                new_reading = models.Reading()
                new_reading.thermocouple_id = sensor['id']
                new_reading.value = end[len(sensor['short_name']):]
                new_reading.date = ndate
                new_reading.save()
                num_new_readings = num_new_readings + 1
    return num_new_readings


# Create your views here.
def update(request):
    return HttpResponse(update_temperatures())


def temperature(request, sensor_name):
    try:
        sensor = models.Thermocouple.objects.get(short_name=sensor_name)
    except models.Thermocouple.DoesNotExist:
        return HttpResponse('sensor not defined', status=404)
    reading = (models.Reading.objects.filter(thermocouple=sensor).
               order_by('-date').values()[0])
    reading['date'] = reading['date'].isoformat()
    return HttpResponse(json.dumps(reading))
