# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.CharField(unique=True, max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=128)),
                ('setLink', models.CharField(max_length=512)),
                ('publishedDate', models.CharField(max_length=32)),
                ('imageLink', models.CharField(max_length=512)),
                ('textSnippet', models.CharField(max_length=1024)),
                ('webReaderLink', models.CharField(max_length=512)),
                ('categories', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('book', models.OneToOneField(to='searchtool.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='query',
            field=models.OneToOneField(null=True, blank=True, to='searchtool.Query'),
            preserve_default=True,
        ),
    ]
