# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_article_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slideritem',
            name='substrate_opacity',
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='substrate_color',
            field=models.CharField(default=b'white', help_text='\u0435\u0441\u043b\u0438 \u043d\u0443\u0436\u043d\u0430 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0442\u043e \u043f\u0438\u0448\u0438\u0442\u0435 RGB \u0446\u0432\u0435\u0442 => rgba(0, 0, 0, 1), \u0433\u0434\u0435 4 \u0430\u0442\u0440\u0438\u0431\u0443\u0442 \u044d\u0442\u043e \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c', max_length=100, verbose_name='\u0426\u0432\u0435\u0442 \u043f\u043e\u0434\u043b\u043e\u0436\u043a\u0438'),
        ),
    ]
