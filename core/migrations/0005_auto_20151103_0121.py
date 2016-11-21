# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151103_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='desc_color',
            field=models.CharField(default=b'black', max_length=10, verbose_name='\u0426\u0432\u0435\u0442 "\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435"'),
        ),
        migrations.AddField(
            model_name='slideritem',
            name='text_color',
            field=models.CharField(default=b'black', max_length=10, verbose_name='\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='slideritem',
            name='title_color',
            field=models.CharField(default=b'black', max_length=10, verbose_name='\u0426\u0432\u0435\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430'),
        ),
    ]
