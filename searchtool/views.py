from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from searchtool.forms import UserForm
from searchtool.dao import daoSaveBookInQuery, daoSaveQueryToUser, daoSaveBookInTopic, \
    daoBookIsLiked, daoSaveLikedBook, daoBookIsCollected, daoSaveBookCart, daoSaveRates, \
    daoCheckRating, daoGetBookCartList, daoSaveBookInTopic, daoGetBookReviews, daoGetTopic, daoGetAllTopic
from searchtool.models import BookCart
from searchtool.models import Query, User

import ast

# This is homepage
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/searchtool/')
            else:
                return HttpResponse("You have not active your account")
        else:
            return HttpResponse("Invalid")
    else:
        return render(request, 'searchtool/index.html', {})

# Register
# user UserForm to register
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    # Render the template depending on the context.
    return render(request,
            'searchtool/register.html',
            {'user_form': user_form, 'registered': registered} )

def profile(request):
    return render(request, 'searchtool/profile.html')

def allTopics(request):
    topicList = daoGetAllTopic()
    return render(request, 'searchtool/alltopics.html', {'topic_list': topicList})

def myTopics(request):
    topicList = daoGetTopic(request.user.username)
    return render(request, 'searchtool/mytopics.html', {'topic_list': topicList})

# Logout
def logoutRequest(request):
    logout(request)
    return HttpResponseRedirect("/searchtool/")

# Search
def search(request):
    # TODO(Integration)
    book_list = [{'id':'Ql6QgWf6i7cC','title':'Thinking In JAVA', 'authors':'Bruce', 'publishedDate':2003, 'setLink':'google.com', 'categories':'computer',
                  'textSnippet':'Bruce Eckel&#39;s &quot;Thinking in Java\-demonstrates advanced topics.Explains sound objectdemonstrates advanced topics.Explains sound objectdemonstrates advanced topics.Explains sound object',
                  'image':'http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
                  'webReaderLink':'http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
                 {'id':'Ql6QgWf6i7cD','title':'Thinking In JAVA2', 'authors':'Bruce', 'publishedDate':2003, 'setLink':'google.com','textSnippet':'something',
                    'image':'http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'categories':'computer',
                  'webReaderLink':'http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
                 {'id':'Ql6QgWf6i7cE','title':'Thinking In JAVA3', 'authors':'Bruce', 'publishedDate':2003, 'setLink':'google.com','textSnippet':'something',
                  'image':'http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'categories':'computer',
                  'webReaderLink':'http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
    ]
    # Process Get information
    # if request.method == 'GET':
    if request.user.is_authenticated() == True:
        # Save queries as user's history into database
        query = daoSaveQueryToUser(request.GET['query'], request.user.username)
        print query
    else:
        query = Query(request.GET['query'], User.objects.get_or_create(username='guest', password='guest'))
    return render(request, 'searchtool/index.html', {'book_list': book_list, 'queryid': query.id})

def goto(request):
    book = ast.literal_eval(request.POST['book'])
    if request.user.is_authenticated() == True:
        # print request.user.username
        daoSaveBookInQuery(book, request.POST['queryid'])
    # Redirect to another page
    # print request
    return HttpResponseRedirect('/searchtool/book?id=%s&&title=%s&&authors=%s&&publishedDate=%s' % (book['id'], book['title'], book['authors'], book['publishedDate']))
    # Discarded
    # print 'goto: ', book['webReaderLink']
    # return HttpResponseRedirect(book['webReaderLink'])

def showBook(request):
    book = {}
    book['id'] = request.GET['id']
    book['title'] = request.GET['title']
    book['authors'] = request.GET['authors']
    book['publishedDate'] = request.GET['publishedDate']
    # book['isLiked'] = daoBookIsLiked(request.GET['id'].encode('utf-8'))
    if(daoBookIsCollected(request.GET['id'], request.user.username) == False):
        book['isCollected'] = "Want to Collect?"
    else:
        book['isCollected'] = "Collected"
    print book['isCollected']
    book['rating'] = daoCheckRating(request.GET['id'].encode('utf-8'), request.user.username)
    book['reviews'] = daoGetBookReviews(request.GET['id'])
    # Session for Collection
    # bookSession = request.session.get('bookCart', [])
    # book['isCollected'] = False
    # for item in bookSession:
    #     if item.get('bookid') == book['id']:
    #         book['isCollected'] = True
    #         break
    # print book['isCollected']
    # book['isCollected'] = request.session
    # print book
    return render(request, 'searchtool/book.html', {'book': book})

def rateBook(request):
    daoSaveRates(request.GET['bookid'], request.GET['rating'], request.user.username)
    rating = daoCheckRating(request.GET['bookid'], request.user.username)
    return HttpResponse(rating)

def collectBook(request):
    daoSaveBookCart(request.GET['bookid'], request.user.username)
    # Session
    # cart = request.session.get("bookCart", [])
    # cart.append(book)
    # request.session['bookCart'] = cart
    # print cart
    # return render(request, 'searchtool/book.html', {'book': book})
    return HttpResponse(True)

# Discarded
def likeBook(request):
    pass
    # daoSaveLikedBook(request.GET['bookid'], request.user.username)
    # return HttpResponse(True)

def addTopic(request):
    bookList = daoGetBookCartList(request.user.username)
    return render(request, 'searchtool/addTopic.html', {'book_list': bookList})

def createTopic(request):
    bookidList = request.POST.getlist('bookid')
    topicTitle = request.POST['topictitle']
    daoSaveBookInTopic(bookidList, request.user.username, topicTitle)
    return HttpResponse(True)
