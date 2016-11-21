# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255,
                                          verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('description', models.TextField(null=True,
                                                 verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
                                                 blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='PersonRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True,
                                              verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u044f\u0432\u043a\u0438')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('email', models.EmailField(max_length=254,
                                            verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430')),
                ('phone_number', models.IntegerField(null=True,
                                                     verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440',
                                                     blank=True)),
                ('message', models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('state', models.BooleanField(default=False,
                                              verbose_name='\u0420\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0443',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('price', models.IntegerField(
                    verbose_name='\u0426\u0435\u043d\u0430 (\u0432 \u0440\u0443\u0431\u043b\u044f\u0445)')),
                ('comment', models.TextField(null=True,
                                             verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                                             blank=True)),
                ('img', models.ImageField(upload_to=b'image-tour/', null=True,
                                          verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                                          blank=True)),
                ('active', models.BooleanField(default=False,
                                               verbose_name='\u0412\u044b\u0434\u0430\u0432\u0430\u0442\u044c \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443')),
                ('category', models.ManyToManyField(to='core.Category',
                                                    verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0442\u0443\u0440',
                'verbose_name_plural': '\u0442\u0443\u0440\u044b',
            },
        ),
    ]
