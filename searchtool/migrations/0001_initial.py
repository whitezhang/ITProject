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
            name='BookCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=128)),
                ('setLink', models.CharField(max_length=512)),
                ('publishedDate', models.CharField(max_length=32)),
                ('imageLink', models.CharField(max_length=512)),
                ('textSnippet', models.CharField(max_length=1024)),
                ('webReaderLink', models.CharField(max_length=512)),
                ('categories', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookItem',
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookLiked',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.CharField(max_length=32)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.CharField(max_length=32)),
                ('rating', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.CharField(unique=True, max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookid', models.CharField(max_length=32)),
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
                ('book', models.ManyToManyField(to='searchtool.BookItem')),
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
            model_name='history',
            name='query',
            field=models.ForeignKey(blank=True, to='searchtool.Query', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookcart',
            name='topic',
            field=models.ForeignKey(blank=True, to='searchtool.Topic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookcart',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
