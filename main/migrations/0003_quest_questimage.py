# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=255)),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(verbose_name='Изображение', upload_to='quest_images/')),
            ],
            options={
                'verbose_name': 'Квест',
                'verbose_name_plural': 'Квесты',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(verbose_name='Изображение', upload_to='quests_images/')),
                ('thumbnail', models.ImageField(verbose_name='Превью 200 на 200', upload_to='preview_quests_images/')),
                ('quest', models.ForeignKey(verbose_name='Квест', to='main.Quest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
