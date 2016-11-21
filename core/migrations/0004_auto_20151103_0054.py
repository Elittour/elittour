# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151103_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='active',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
    ]
