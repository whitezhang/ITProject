from django.contrib import admin
from searchtool.models import UserProfile, Book, Query, Topic

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Query)
admin.site.register(Topic)