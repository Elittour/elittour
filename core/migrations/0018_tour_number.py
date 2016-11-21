# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_article_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='number',
            field=models.IntegerField(default=1, help_text='\u0414\u043b\u044f \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 , \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0438\u0437 \u0434\u0430\u0442\u044b', verbose_name='\u041a\u043e\u0434'),
            preserve_default=False,
        ),
    ]
