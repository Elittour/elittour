# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151109_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='substrate_color',
            field=models.CharField(default=b'white', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u043f\u043e\u0434\u043b\u043e\u0436\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='slideritem',
            name='substrate_opacity',
            field=models.CharField(default=b'1', help_text='\u041e\u0442 0 \u0434\u043e 1 (0.5 , 0.45 \u0438 \u0442\u0434)', max_length=100, verbose_name='\u041d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u044c \u043f\u043e\u0434\u043b\u043e\u0436\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='desc_color',
            field=models.CharField(default=b'black', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 "\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435"'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='text_color',
            field=models.CharField(default=b'black', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='title_color',
            field=models.CharField(default=b'black', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430'),
        ),
    ]
