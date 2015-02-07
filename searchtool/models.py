from django.db import models

# Create your models here.

# User
class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    def __unicode__(self):
        return self.username

# History
class History(models.Model):
    query = models.CharField(max_length=512)        # same query can do recommendation
    date = models.DateField()
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.query

# Topic
class Topic(models.Model):
    topic = models.CharField(max_length=32)
    date = models.DateField()
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.topic

# Query
class Query(models.Model):
    query = models.CharField(max_length=512)
    topic = models.ForeignKey(Topic, blank=True, null=True)

    def __unicode__(self):
        return self.query

# Result
class Result(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    url = models.CharField(max_length=512)
    query = models.ForeignKey(Query, blank=True, null=True)

    def __unicode__(self):
        return self.title


