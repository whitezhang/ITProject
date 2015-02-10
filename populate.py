__author__ = 'wyatt'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchWeb.settings')

import django
django.setup()

from searchtool.models import UserProfile

def populate():
    addUser("Wyatt", "123456")


def addUser(username, password):
    u = UserProfile.objects.get_or_create(username=username,password=password)[0]
    return u

if __name__ == '__main__':
    print "Searchtool population"
    populate()