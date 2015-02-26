__author__ = 'wyatt'

from django.contrib.auth.models import User
from searchtool.models import Query, UserProfile, Book

def daoSaveBookInQuery(book, queryid):
    # print queryid
    q = Query.objects.get(id=queryid)
    b = Book.objects.get_or_create(bookid=book['id'], title=book['title'], authors=book['authors'], setLink=book['setLink'],
             publishedDate=book['publishedDate'], imageLink=book['image'], textSnippet=book['textSnippet'],
             webReaderLink=book['webReaderLink'], categories=book['categories'], query=q)
    # False means getting
    print b[0].views
    if b[1] == False:
        b[0].views = 1+b[0].views
        print 'to: ', b[0].views
        b[0].save()

# Save query to user
# @return query
def daoSaveQueryToUser(query, username):
    u = User.objects.get(username=username)
    q = Query(query=query, user=u)
    q.save()
    return q


def saveBookInTopic():
    pass
