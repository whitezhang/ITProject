from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User: Discarded
class UserProfile(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    # user = models.OneToOneField(User)

    def __unicode__(self):
        return self.username
        # return self.user.username

# Query
# ER: query <--> many to one <--> user
class Query(models.Model):
    query = models.CharField(max_length=128)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.query

# BookLiked
#ER:
class BookLiked(models.Model):
    bookid = models.CharField(max_length=32, unique=True)
    def __unicode__(self):
        return self.bookid

# BookReview
# primary key: bookid
class BookReview(models.Model):
    bookid = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=1)

    def __unicode__(self):
        return self.title

# Book
# ER: book <--> one to one <--> query
class Book(models.Model):
    bookid = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    authors = models.CharField(max_length=128)
    setLink = models.CharField(max_length=512)
    publishedDate = models.CharField(max_length=32)
    imageLink = models.CharField(max_length=512)
    textSnippet = models.CharField(max_length=1024)
    webReaderLink = models.CharField(max_length=512)
    categories = models.CharField(max_length=128)

    views = models.IntegerField(default=1)

    # query = models.OneToOneField(Query, blank=True, null=True)
    query = models.ForeignKey(Query, blank=True, null=True)

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