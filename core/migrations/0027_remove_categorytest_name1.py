# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_delete_categorytest1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytest',
            name='name1',
        ),
    ]
