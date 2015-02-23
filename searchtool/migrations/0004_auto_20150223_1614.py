# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0003_book_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bid',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
