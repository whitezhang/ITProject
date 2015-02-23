from django.db import models

# Create your models here.

# User
class UserProfile(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    def __unicode__(self):
        return self.username

# Query
# ER: query <--> many to one <--> user
class Query(models.Model):
    query = models.CharField(max_length=128)

    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.query

# Book
# ER: book <--> one to one <--> query
class Book(models.Model):
    bookid = models.CharField(max_length=32,unique=True)
    title = models.CharField(max_length=128)
    authors = models.CharField(max_length=128)
    setLink = models.CharField(max_length=512)
    publishedDate = models.CharField(max_length=32)
    imageLink = models.CharField(max_length=512)
    textSnippet = models.CharField(max_length=1024)
    webReaderLink = models.CharField(max_length=512)
    categories = models.CharField(max_length=128)

    views = models.IntegerField(default=0)

    query = models.OneToOneField(Query, blank=True, null=True)

    def __unicode__(self):
        return self.title

# Topic
# ER : topic <--> one to many <--> book
class Topic(models.Model):
    topic = models.CharField(max_length=32)
    date = models.DateField()

    book = models.OneToOneField(Book)

    def __unicode__(self):
        return self.topic