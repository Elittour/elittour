# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151109_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='active_for_last',
            new_name='active_for_right',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='active_for_last',
            new_name='active_for_right',
        ),
    ]
