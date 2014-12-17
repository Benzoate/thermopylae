from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def temperature(request, sensor_name):
    return HttpResponse('YOLO')
