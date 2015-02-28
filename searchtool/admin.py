from django.contrib import admin
from searchtool.models import UserProfile, Book, Query, Topic, BookReview, BookLiked, BookCart

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(Query)
admin.site.register(Topic)
admin.site.register(BookLiked)
admin.site.register(BookCart)
