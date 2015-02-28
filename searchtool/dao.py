__author__ = 'wyatt'

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from searchtool.models import Query, UserProfile, Book, BookReview, BookLiked, BookCart, BookRating

def daoSaveBookInQuery(book, queryid):
    # print queryid
    q = Query.objects.get(id=queryid)
    b = Book.objects.get_or_create(bookid=book['id'], title=book['title'], authors=book['authors'], setLink=book['setLink'],
             publishedDate=book['publishedDate'], imageLink=book['image'], textSnippet=book['textSnippet'],
             webReaderLink=book['webReaderLink'], categories=book['categories'], query=q)
    br = BookReview.objects.get_or_create(bookid=book['id'], title=book['title'])
    # False means getting
    # Book
    if b[1] == False:
        b[0].views += 1
        b[0].save()
    # BookReview
    if br[1] == False:
        br[0].views += 1
        br[0].save()

# Save query to user
# @return query
def daoSaveQueryToUser(query, username):
    u = User.objects.get(username=username)
    q = Query(query=query, user=u)
    q.save()
    return q

def daoBookIsLiked(bookid):
    try:
        b = BookLiked.objects.get(bookid=bookid)
    except ObjectDoesNotExist:
        return False
    return True

def daoBookIsCollected(bookid):
    try:
        b = BookCart.objects.get(bookid=bookid)
    except ObjectDoesNotExist:
        return False
    return True

def daoCheckRating(bookid, username):
    u = User.objects.get(username=username)
    b = BookRating.objects.filter(bookid=bookid, user=u)
    print bookid, u
    print b
    # Has not rated this book
    if len(b) == 0:
        return -1
    number = BookRating.objects.filter(bookid=bookid).count()
    sum = BookRating.objects.filter(bookid=bookid).aggregate(Sum('rating'))
    print 'rate'
    print sum['rating__sum']/number
    return round(sum['rating__sum']/number)

def daoSaveRates(bookid, rating, username):
    u = User.objects.get(username=username)
    # Has rated this book, can not rate it again
    if daoCheckRating(bookid, username) != -1:
        return
    br = BookRating.objects.get_or_create(bookid=bookid, rating=rating, user=u)
    br[0].save()

def daoSaveBookCart(bookid, username):
    u = User.objects.get(username=username)
    bookLib = Book.objects.filter(bookid=bookid)[0]
    bc = BookCart.objects.get_or_create(bookid=bookLib.bookid, title=bookLib.title, authors=bookLib.authors, setLink=bookLib.setLink,
             publishedDate=bookLib.publishedDate, imageLink=bookLib.imageLink, textSnippet=bookLib.textSnippet,
             webReaderLink=bookLib.webReaderLink, categories=bookLib.categories, user=u)
    bc[0].save()

def daoSaveBookInTopic():
    pass

def daoSaveLikedBook(bookid, username):
    print bookid
    u = User.objects.get(username=username)
    lb = BookLiked.objects.get_or_create(bookid='Ql6QgWf6i7cE', user=u)
    lb[0].save()