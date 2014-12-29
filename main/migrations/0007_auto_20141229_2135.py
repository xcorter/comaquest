# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20141228_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'Описание', 'verbose_name': 'Описание'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Контакты', 'verbose_name': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Бронирование', 'verbose_name': 'Бронирование'},
        ),
        migrations.AlterModelOptions(
            name='questimage',
            options={'verbose_name_plural': 'Изображения квестов', 'verbose_name': 'Изображение квестов'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Изображения слайдера', 'verbose_name': 'Изображение слайдера'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name_plural': 'Время', 'verbose_name': 'Время'},
        ),
        migrations.AlterField(
            model_name='about',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Описание проекта'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Контакты'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questimage',
            name='thumbnail',
            field=models.ImageField(upload_to='preview_quests_images/', verbose_name='Превью 121 на 110'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
            preserve_default=True,
        ),
    ]
