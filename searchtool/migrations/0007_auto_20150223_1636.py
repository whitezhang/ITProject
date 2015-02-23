# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0006_book_query'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bid',
            new_name='bookid',
        ),
    ]
