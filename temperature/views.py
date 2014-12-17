from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.
def temperature(request, sensor_name):
    r = requests.get('http://aaronlockton.com/xrf.txt')
    lines = r.text.split('\n')
    vals = []
    for line in lines:
        parts = line.split(' ')
        if len(parts) < 3:
            continue
        if sensor_name in parts[2]:
            temp = (parts[2][len(sensor_name):])
            vals.append({'temperature': temp, 'date': parts[0]})
    return HttpResponse(json.dumps(vals))
