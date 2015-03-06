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
# ER:
class BookLiked(models.Model):
    bookid = models.CharField(max_length=32)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.bookid

# BookRating
class BookRating(models.Model):
    bookid = models.CharField(max_length=32)
    rating = models.IntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username+": "+self.bookid

# BookReview
# primary key: bookid
class BookReview(models.Model):
    bookid = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=1)

    def __unicode__(self):
        return self.title

#History
class History(models.Model):
    bookid = models.CharField(max_length=32)
    query = models.ForeignKey(Query, blank=True, null=True)

    def __unicode__(self):
        return self.bookid

class BookItem(models.Model):
    bookid = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=128)
    authors = models.CharField(max_length=128)
    setLink = models.CharField(max_length=512)
    publishedDate = models.CharField(max_length=32)
    imageLink = models.CharField(max_length=512)
    textSnippet = models.CharField(max_length=1024)
    description = models.CharField(max_length=2048)
    webReaderLink = models.CharField(max_length=512)
    categories = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

# Book
# Once clicked
# ER: book <--> many to one <--> query
# class Book(models.Model):
#     bookid = models.CharField(max_length=32)
#     title = models.CharField(max_length=128)
#     authors = models.CharField(max_length=128)
#     setLink = models.CharField(max_length=512)
#     publishedDate = models.CharField(max_length=32)
#     imageLink = models.CharField(max_length=512)
#     textSnippet = models.CharField(max_length=1024)
#     webReaderLink = models.CharField(max_length=512)
#     categories = models.CharField(max_length=128)
#
#     views = models.IntegerField(default=1)
#
#     query = models.ForeignKey(Query, blank=True, null=True)
#     # query = models.ForeignKey(Query)
#     # bookCart = models.ForeignKey(BookCart, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.title

# Topic
# ER : topic <--> many to many <--> book
class Topic(models.Model):
    topic = models.CharField(max_length=32)
    date = models.DateTimeField()

    book = models.ManyToManyField(BookItem)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.topic

# Shopping cart
class BookCart(models.Model):
    bookid = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    authors = models.CharField(max_length=128)
    setLink = models.CharField(max_length=512)
    publishedDate = models.CharField(max_length=32)
    imageLink = models.CharField(max_length=512)
    textSnippet = models.CharField(max_length=1024)
    webReaderLink = models.CharField(max_length=512)
    categories = models.CharField(max_length=128)

    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic, blank=True, null=True)

    def __unicode__(self):
        return self.user.username+": "+self.title

