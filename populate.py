__author__ = 'wyatt'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchWeb.settings')

import django
django.setup()

from searchtool.models import UserProfile, BookItem
from searchtool.app import bookJSONParser

def populate():
    bookName = ['java', 'python', 'django', 'test', 'cook', 'math']
    for name in bookName:
        book = bookJSONParser(name)
        for b in book:
            addBook(b['id'], b['title'], b['authors'], b['setLink'], b['publishedDate'], b['image'], b['textSnippet'], b['description'], b['webReaderLink'], b['categories'])


def addUser(username, password):
    u = UserProfile.objects.get_or_create(username=username,password=password)[0]
    return u

def addBook(bookid, title, authors, setLink, publishedDate, imageLink, textSnippet, description, webReaderLink, categories):
    b = BookItem.objects.get_or_create(bookid=bookid,title=title,authors=authors,setLink=setLink,publishedDate=publishedDate,imageLink=imageLink,
                                   textSnippet=textSnippet,description=description,webReaderLink=webReaderLink,categories=categories)[0]
    return b

if __name__ == '__main__':
    print "Searchtool population"
    populate()