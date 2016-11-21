# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151103_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='active_for_last',
            field=models.BooleanField(default=False, verbose_name='\u0412\u044b\u0434\u0430\u0432\u0430\u0442\u044c \u0432 \u043f\u0440\u0430\u0432\u043e\u043c \u0431\u043b\u043e\u043a\u0435'),
        ),
    ]
