# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20141229_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
            preserve_default=True,
        ),
    ]
