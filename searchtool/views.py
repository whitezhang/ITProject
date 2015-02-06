from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from searchtool.form import LoginForm
from django.contrib.auth import authenticate, login

# This is homepage
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print username, password

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/searchtool/')
            else:
                return HttpResponse("Error")
        else:
            return HttpResponse("Invalid")
    else:
        return render(request, 'searchtool/index.html', {})
