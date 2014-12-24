# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0003_collatedreading'),
    ]

    operations = [
        migrations.AddField(
            model_name='collatedreading',
            name='thermocouple',
            field=models.ForeignKey(default=None, to='temperature.Thermocouple'),
            preserve_default=False,
        ),
    ]
