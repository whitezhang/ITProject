# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0003_auto_20150225_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookid',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='query',
            field=models.ForeignKey(blank=True, to='searchtool.Query', null=True),
            preserve_default=True,
        ),
    ]
