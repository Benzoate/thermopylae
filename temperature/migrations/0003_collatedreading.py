# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0002_auto_20141217_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollatedReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('mean', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
