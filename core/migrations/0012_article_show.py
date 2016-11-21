# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20151109_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c'),
        ),
    ]
