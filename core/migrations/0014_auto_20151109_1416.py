# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20151109_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedTour',
            fields=[
                ('tour_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Tour')),
            ],
            options={
                'verbose_name': '\u0442\u0443\u0440',
                'verbose_name_plural': '\u0442\u0443\u0440\u044b',
            },
            bases=('core.tour',),
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': '\u0430\u0432\u0442\u043e\u0431\u0443\u0441\u043d\u044b\u0439 \u0442\u0443\u0440', 'verbose_name_plural': '\u0430\u0432\u0442\u043e\u0431\u0443\u0441\u043d\u044b\u0435 \u0442\u0443\u0440\u044b'},
        ),
    ]
