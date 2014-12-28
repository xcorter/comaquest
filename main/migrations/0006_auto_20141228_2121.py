# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20141228_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(verbose_name='Комментарий', default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='participant_amount',
            field=models.IntegerField(verbose_name='Телефон', max_length=2, default=0),
            preserve_default=True,
        ),
    ]
