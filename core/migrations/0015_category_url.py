# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20151109_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default=1, max_length=255, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0435\u0439'),
            preserve_default=False,
        ),
    ]
