__author__ = 'wyatt'

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from searchtool.models import Query, UserProfile, BookReview, BookLiked, BookCart, BookRating, BookItem, History, Topic
import datetime

def daoGetReviewedBookByIDs(IDs):
    return BookReview.objects.filter(bookid__in=IDs).order_by('-views')[:10]

def daoGetIDsByCategory(category):
    return BookItem.objects.values_list('bookid', flat=True).filter(categories__icontains=category)

def daoSaveBookInQuery(book, queryid):
    # print queryid
    q = Query.objects.get(id=queryid)
    b = BookItem.objects.get_or_create(bookid=book['id'], title=book['title'], authors=book['authors'], setLink=book['setLink'],
             publishedDate=book['publishedDate'], imageLink=book['image'], textSnippet=book['textSnippet'],
             webReaderLink=book['webReaderLink'], description=book['description'], categories=book['categories'])
    b[0].save()
    h = History.objects.get_or_create(bookid=book['id'], query=q)
    h[0].save()
    # Save in the BookReview
    daoSaveBookReview(book['id'], book['title'])

def daoSaveBookReview(bookid, title):
    br = BookReview.objects.get_or_create(bookid=bookid, title=title)
    # False means not exist in the BookReview
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

def daoBookIsCollected(bookid, username):
    u = User.objects.get(username=username)
    try:
        b = BookCart.objects.get(bookid=bookid, user=u)
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
    # print sum['rating__sum']/number
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
    bookLib = BookItem.objects.filter(bookid=bookid)[0]
    bc = BookCart.objects.get_or_create(bookid=bookLib.bookid, title=bookLib.title, authors=bookLib.authors, setLink=bookLib.setLink,
             publishedDate=bookLib.publishedDate, imageLink=bookLib.imageLink, textSnippet=bookLib.textSnippet,
             webReaderLink=bookLib.webReaderLink, categories=bookLib.categories, user=u)
    bc[0].save()

def daoGetBookCartList(username):
    u = User.objects.get(username=username)
    blist = BookCart.objects.filter(user=u)
    return blist

# Create a topic from book cart
# Then delete these books from cart
def daoSaveBookInTopic(bookidList, username, topicTitle):
    u = User.objects.get(username=username)
    t = Topic(topic=topicTitle, date=datetime.datetime.today(), user=u)
    t.save()
    for id in bookidList:
        b = BookItem.objects.get(bookid=id)
        t.book.add(b)
        BookCart.objects.get(bookid=id, user=u).delete()

# def daoSaveLikedBook(bookid, username):
#     u = User.objects.get(username=username)
#     lb = BookLiked.objects.get_or_create(bookid='Ql6QgWf6i7cE', user=u)
#     lb[0].save()

def daoGetBookReviews(bookid):
    br = BookReview.objects.get(bookid=bookid)
    return br.views

def daoGetReviewedBook():
    return BookReview.objects.order_by('-views')[:10]

def daoGetTopicByUser(username):
    u = User.objects.get(username=username)
    topicList = Topic.objects.filter(user=u)
    return topicList

def daoGetAllCategories():
    value_list = BookItem.objects.values_list('categories', flat=True).distinct()
    ret_list = []
    for value in value_list:
        # Split method needs test
        for item in value[2:-2].split("', '"):
            ret_list.append(item)
    return ret_list

def daoGetAllTopic():
    return Topic.objects.all()

def daoGetBookByID(bookid):
    b = BookItem.objects.get(bookid=bookid)
    return b

# Get topic according to id
def daoGetTopicByID(topicid):
    return Topic.objects.get(id=topicid)

def daoRemoveFromCartByID(bookid, username):
    u = User.objects.get(username=username)
    BookCart.objects.get(bookid=bookid, user=u).delete()


