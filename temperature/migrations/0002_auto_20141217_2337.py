# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reading',
            old_name='temperature',
            new_name='thermocouple',
        ),
    ]
