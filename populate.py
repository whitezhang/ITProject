__author__ = 'wyatt'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchWeb.settings')

import django
django.setup()

from searchtool.models import UserProfile, Book

def populate():
    addUser("Wyatt", "123456")
    addBook("Ql6QgWf6i7cC", "Thinking In Java", "someone", "setlinks", "2001", "imagelink", "snippet", "webreader", "computers", 0)


def addUser(username, password):
    u = UserProfile.objects.get_or_create(username=username,password=password)[0]
    return u

def addBook(bookid, title, authors, setLink, publishedDate, imageLink, textSnippet, webReaderLink, categories, views):
    b = Book.objects.get_or_create(bookid=bookid,title=title,authors=authors,setLink=setLink,publishedDate=publishedDate,imageLink=imageLink,
                                   textSnippet=textSnippet,webReaderLink=webReaderLink,categories=categories,views=views)[0]
    return b

if __name__ == '__main__':
    print "Searchtool population"
    populate()