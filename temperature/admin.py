from django.contrib import admin
from temperature import models


@admin.register(models.Thermocouple)
class ThermocoupleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Reading)
class ReadingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CollatedReading)
class CollatedReadingAdmin(admin.ModelAdmin):
    pass
