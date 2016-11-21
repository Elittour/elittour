# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_slideritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideritem',
            name='text',
            field=models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='title',
            field=models.TextField(verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
