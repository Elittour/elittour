# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20151201_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytest',
            name='name1',
            field=models.CharField(default=datetime.datetime(2015, 12, 1, 16, 27, 31, 46000, tzinfo=utc), max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
            preserve_default=False,
        ),
    ]
