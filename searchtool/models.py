from django.db import models

# Create your models here.

# History
class History(models.Model):
    query = models.CharField(max_length=512)        # same query can do recommendation
    date = models.DateField()

    def __unicode__(self):
        return self.query

# Result
class Result(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    url = models.CharField(max_length=512)

    def __unicode__(self):
        return self.title

# Query
class Query(models.Model):
    query = models.CharField(max_length=512)
    result = models.ForeignKey(Result)

    def __unicode__(self):
        return self.query

# Topic
class Topic(models.Model):
    topic = models.CharField(max_length=32)
    date = models.DateField()
    query = models.ForeignKey(Query)

    def __unicode__(self):
        return self.topic

# User
class User(models.Model):
    uid = models.IntegerField(unique=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    history = models.ForeignKey(History)
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.username
