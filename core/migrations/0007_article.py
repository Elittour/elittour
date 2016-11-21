# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_tour_active_for_last'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.TextField(verbose_name='\u0421\u0442\u0430\u0442\u044c\u044f')),
                ('img', models.ImageField(upload_to=b'image-tour/', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                ('active_for_last', models.BooleanField(default=False, verbose_name='\u0412\u044b\u0434\u0430\u0432\u0430\u0442\u044c \u0432 \u043f\u0440\u0430\u0432\u043e\u043c \u0431\u043b\u043e\u043a\u0435')),
                ('category', models.ManyToManyField(to='core.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0430\u044c\u044e',
                'verbose_name_plural': '\u0441\u0442\u0430\u0442\u044c\u0438',
            },
        ),
    ]
