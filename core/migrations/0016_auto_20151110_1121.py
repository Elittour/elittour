# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_category_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slideritem',
            name='url',
        ),
        migrations.AddField(
            model_name='slideritem',
            name='category',
            field=models.ForeignKey(blank=True, to='core.Category', help_text='\u0411\u0443\u0434\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0435\u0439', null=True, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
    ]
