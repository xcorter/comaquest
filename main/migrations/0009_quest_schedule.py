# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150105_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='schedule',
            field=models.ManyToManyField(verbose_name='Время', to='main.Time', null=True),
            preserve_default=True,
        ),
    ]
