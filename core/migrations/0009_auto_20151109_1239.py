# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='color_date',
            field=models.CharField(default=b'black', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u0434\u0430\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='tour',
            name='color_name',
            field=models.CharField(default=b'black', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='tour',
            name='color_price',
            field=models.CharField(default=b'black', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u0446\u0435\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='date',
            field=models.DateField(max_length=100, verbose_name='\u0414\u0430\u0442\u0430'),
        ),
    ]
