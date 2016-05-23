# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('cost_price', models.FloatField(null=True, blank=True)),
                ('sell_price', models.FloatField(null=True, blank=True)),
                ('qty', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
