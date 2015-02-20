from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from searchtool.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from searchtool.forms import UserProfile
from searchtool.forms import UserForm

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