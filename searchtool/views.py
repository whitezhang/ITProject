from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from searchtool.forms import UserForm
from searchtool.dao import daoSaveBookInQuery, daoSaveQueryToUser, daoSaveBookInTopic, \
    daoBookIsLiked, daoBookIsCollected, daoSaveBookCart, daoSaveRates, \
    daoCheckRating, daoGetBookCartList, daoSaveBookInTopic, daoGetBookReviews, daoGetTopicByUser,\
    daoGetAllTopic, daoGetBookByID, daoGetTopicByID, daoRemoveFromCartByID, daoGetReviewedBook, \
    daoGetAllCategories, daoSaveBookReview, daoGetIDsByCategory, daoGetReviewedBookByIDs
from searchtool.models import BookCart
from searchtool.models import Query, User
from searchtool.app import bookJSONParser, relatedBookCrawler, taxonomyGenerator

import ast

# This is homepage
def index(request):
    categories = daoGetAllCategories()
    if 'categories' in request.GET:
        IDs = daoGetIDsByCategory(request.GET['categories'])
        print IDs
        popularBooks = daoGetReviewedBookByIDs(IDs)
        return render(request, 'searchtool/index.html', {'popular_books': popularBooks, 'categories': categories})
    else:
        popularBooks = daoGetReviewedBook()
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
            return render(request, 'searchtool/index.html', {'popular_books': popularBooks, 'categories': categories})

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
    if 'ouser' in request.GET:
        u = request.GET['ouser']
        topicList = daoGetTopicByUser(request.GET['ouser'])
        # ontologyJSON = taxonomyGenerator(request.GET['ouser'])
    else:
        u = request.user.username
        topicList = daoGetTopicByUser(request.user.username)
        # ontologyJSON = taxonomyGenerator(request.user.username)
    # ontologyJSON = '{id:190,name:"PearlJam",children:[{id:84,name:"PearlJam&amp;CypressHill",children:[{id:82,name:"CypressHill",children:[]}]},],}'
    ontologyJSON = "{'children': [{'children': [{'children': [{'id': 27456, 'name': 'comics'}], 'id': 17777, 'name': '&nbsp;&nbsp;&nbsp;comics<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and<br>&nbsp;&nbsp;animation<br>'}, {'id': 16804, 'name': 'books and literature'}], 'id': 9041, 'name': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;art<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and<br>&nbsp;&nbsp;entertainment<br>'}], 'id': 0, 'name': 'Me'}"
    return render(request, 'searchtool/profile.html', {'ontologyJSON': ontologyJSON, 'topic_list': topicList, 'name': u})

def allTopics(request):
    topicList = daoGetAllTopic()
    curPage = 1
    if 'page' in request.GET:
        curPage = int(request.GET['page'])
    numOfTopic = len(topicList)
    numOfTopicForPage = 10
    # Control the Topic list
    reversedTopicList = []
    for index in range(numOfTopic):
        reversedTopicList.append(topicList[numOfTopic-index-1])
    topicList = reversedTopicList[(curPage-1)*numOfTopicForPage:curPage*numOfTopicForPage]
    # Control the page
    numOfPages = numOfTopic/numOfTopicForPage
    if numOfTopic%numOfTopicForPage != 0:
        numOfPages += 1
    if numOfPages > 5:
        numOfPages = 5
    if curPage <= 2:
        pageInfo = range(1,numOfPages+1)
    elif curPage+1 >= numOfPages:
        pageInfo = range(numOfPages-4, numOfPages+1)
    else:
        pageInfo = range(curPage-2, curPage+3)
    return render(request, 'searchtool/alltopics.html', {'topic_list': topicList, 'cur_page': curPage, 'num_pages':numOfPages, 'page_info': pageInfo})

def myTopics(request):
    topicList = daoGetTopicByUser(request.user.username)
    curPage = 1
    if 'page' in request.GET:
        curPage = int(request.GET['page'])
    numOfTopic = len(topicList)
    numOfTopicForPage = 10
    # Control the Topic list
    reversedTopicList = []
    for index in range(numOfTopic):
        reversedTopicList.append(topicList[numOfTopic-index-1])
    topicList = reversedTopicList[(curPage-1)*numOfTopicForPage:curPage*numOfTopicForPage]
    # Control the page
    numOfPages = numOfTopic/numOfTopicForPage
    if numOfTopic%numOfTopicForPage != 0:
        numOfPages += 1
    if numOfPages > 5:
        numOfPages = 5
    if curPage <= 2:
        pageInfo = range(1,numOfPages+1)
    elif curPage+1 >= numOfPages:
        pageInfo = range(numOfPages-4, numOfPages+1)
    else:
        pageInfo = range(curPage-2, curPage+3)
    # return render(request, 'searchtool/mytopics.html', {'topic_list': topicList})
    return render(request, 'searchtool/mytopics.html', {'topic_list': topicList, 'cur_page': curPage, 'num_pages':numOfPages, 'page_info': pageInfo})

# Logout
def logoutRequest(request):
    logout(request)
    return HttpResponseRedirect("/searchtool/")

# Search
def search(request):
    query = request.GET['query']
    book_list = bookJSONParser(query)
    # Process Get information
    # if request.method == 'GET':
    if request.user.is_authenticated() == True:
        # Save queries as user's history into database
        query = daoSaveQueryToUser(query, request.user.username)
    else:
        query = Query(query, User.objects.get_or_create(username='guest', password='guest'))
    return render(request, 'searchtool/index.html', {'book_list': book_list, 'queryid': query.id})

def gotoBook(request):
    if request.user.is_authenticated() == False:
        return render(request, 'searchtool/error.html')
    if 'book' in request.POST:
        book = ast.literal_eval(request.POST['book'])
        if request.user.is_authenticated() == True:
            # print request.user.username
            if 'queryid' in request.POST['queryid']:
                daoSaveBookInQuery(book, request.POST['queryid'])
            # Redirect to another page
            # print request
                return HttpResponseRedirect('/searchtool/book?id=%s&title=%s&authors=%s&publishedDate=%s&queryid=%s' % (book['id'], book['title'], book['authors'], book['publishedDate'], request.POST['queryid']))
        return HttpResponseRedirect('/searchtool/book?id=%s&title=%s&authors=%s&publishedDate=%s' % (book['id'], book['title'], book['authors'], book['publishedDate']))
    else:
        daoSaveBookReview(request.GET['id'], request.GET['title'])
        return HttpResponseRedirect('/searchtool/book?id=%s&title=%s' % (request.GET['id'], request.GET['title']))
    # Discarded
    # print 'goto: ', book['webReaderLink']
    # return HttpResponseRedirect(book['webReaderLink'])

def showBook(request):
    book = {}
    book['id'] = request.GET['id']
    book['title'] = request.GET['title']
    bookItem = daoGetBookByID(book['id'])

    queryid = ''
    if 'queryid' in request.GET:
        queryid = request.GET['queryid']

    if 'authors' in request.GET and 'publishedDate' in request.GET:
        book['authors'] = request.GET['authors'].encode('utf-8')
        book['publishedDate'] = request.GET['publishedDate']
    else:
        book['authors'] = bookItem.authors
        book['publishedDate'] = bookItem.publishedDate
    if(daoBookIsCollected(request.GET['id'], request.user.username) == False):
        book['isCollected'] = "Want to Collect?"
    else:
        book['isCollected'] = "Collected"
    book['rating'] = daoCheckRating(request.GET['id'].encode('utf-8'), request.user.username)
    book['reviews'] = daoGetBookReviews(request.GET['id'])
    book['image'] = bookItem.imageLink
    book['description'] = bookItem.description

    # Crawl the related books
    relatedBook = relatedBookCrawler(book['title'])
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
    return render(request, 'searchtool/book.html', {'book': book, 'related_book': relatedBook, 'queryid': queryid})

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
    # print bookidList, topicTitle
    daoSaveBookInTopic(bookidList, request.user.username, topicTitle)
    topicList = daoGetAllTopic()
    return render(request, 'searchtool/alltopics.html', {'topic_list': topicList, 'created': 'true', 'topic_title': topicTitle})

# show topic according to the topic id
def showTopic(request):
    topic = daoGetTopicByID(request.GET['id'])
    book = []
    for b in topic.book.all():
        # item = {}
        # item['title'] = b.title
        # item['webReaderLink'] = b.webReaderLink
        # item['image'] = b.imageLink
        tmpBook = {}
        tmpBook['id'] = b.bookid
        tmpBook['title'] = b.title
        tmpBook['authors'] = b.authors
        tmpBook['setLink'] = b.setLink
        tmpBook['publishedDate'] = b.publishedDate
        tmpBook['imageLink'] = b.imageLink
        tmpBook['textSnippet'] = b.textSnippet
        tmpBook['description'] = b.description
        tmpBook['webReaderLink'] = b.webReaderLink
        tmpBook['categories'] = b.categories
        book.append(tmpBook)
    # print book
    topicInfo = {}
    topicInfo['id'] = topic.id
    topicInfo['date'] = topic.date
    topicInfo['topic'] = topic.topic
    topicInfo['user'] = topic.user.username
    topicInfo['book'] = book
    return render(request, 'searchtool/topic.html', {'topic_info': topicInfo})

def removeFromCart(request):
    daoRemoveFromCartByID(request.GET['bookid'], request.user.username)
    return HttpResponse(True)
