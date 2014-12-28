# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Дата')),
                ('first_name', models.CharField(verbose_name='Имя', max_length=100)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=100)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=75)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=50)),
                ('quest', models.ForeignKey(to='main.Quest', verbose_name='Квест')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time', models.CharField(verbose_name='Время', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.ForeignKey(to='main.Time', verbose_name='Время'),
            preserve_default=True,
        ),
    ]
