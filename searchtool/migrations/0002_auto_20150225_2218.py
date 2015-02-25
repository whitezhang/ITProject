# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='user',
            field=models.ForeignKey(to='searchtool.UserProfile'),
            preserve_default=True,
        ),
    ]
