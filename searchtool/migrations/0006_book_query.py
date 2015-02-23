# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0005_auto_20150223_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='query',
            field=models.OneToOneField(null=True, blank=True, to='searchtool.Query'),
            preserve_default=True,
        ),
    ]
