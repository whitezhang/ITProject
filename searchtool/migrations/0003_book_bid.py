# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0002_remove_book_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bid',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
