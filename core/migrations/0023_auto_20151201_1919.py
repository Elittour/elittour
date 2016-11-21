# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20151201_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', blank=True)),
                ('url', models.CharField(max_length=255, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0441 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0435\u0439')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e1',
                'verbose_name_plural': '\u043a\u0442\u0435\u0433\u043e\u0440\u0438\u04381',
            },
        ),
        migrations.DeleteModel(
            name='CategoryTest2',
        ),
    ]
