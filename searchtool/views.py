from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from searchtool.forms import UserForm
from searchtool.dao import daoSaveBookInQuery, daoSaveQueryToUser, saveBookInTopic
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

# Logout
def logoutRequest(request):
    logout(request)
    return HttpResponseRedirect("/searchtool/")

# Search
def search(request):
    # TODO
    book_list = [{'id':'Ql6QgWf6i7cC','title':'Thinking In JAVA', 'authors':'Bruce', 'publishedDate':2003, 'setLink':'google.com', 'categories':'computer',
                  'textSnippet':'Bruce Eckel&#39;s &quot;Thinking in Java\-demonstrates advanced topics.Explains sound objectdemonstrates advanced topics.Explains sound objectdemonstrates advanced topics.Explains sound object',
                  'image':'http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
                  'webReaderLink':'http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
                 {'id':'Ql6QgWf6i7cC','title':'Thinking In JAVA2', 'authors':'Bruce', 'publishedDate':2003, 'setLink':'google.com','textSnippet':'something',
                  'image':'http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'categories':'computer',
                  'webReaderLink':'http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
                 {'id':'Ql6QgWf6i7cC','title':'Thinking In JAVA3', 'authors':'Bruce', 'publishedDate':2003, 'setLink':'google.com','textSnippet':'something',
                  'image':'http://books.google.com/books/content?id=Ql6QgWf6i7cC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'categories':'computer',
                  'webReaderLink':'http://books.google.co.uk/books/reader?id=Ql6QgWf6i7cC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
    ]
    # Process Get information
    if request.method == 'GET':
        # Save queries as user's history into database
        query = daoSaveQueryToUser(request.GET['query'], request.user.username)
        print query
    return render(request, 'searchtool/index.html', {'book_list': book_list, 'queryid': query.id})

def goto(request):
    book = ast.literal_eval(request.POST['book'])
    print request.POST['queryid']
    # query = ast.literal_eval(request.POST['query'][0])
    # print query.id
    if request.user.is_authenticated() == True:
        print request.user.username
        # print type(request.POST['query'])
        daoSaveBookInQuery(book, request.POST['queryid'])
    print 'goto: ', request.POST['readerLink']
    return HttpResponseRedirect(request.POST['readerLink'])
