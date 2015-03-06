from django.contrib import admin
from searchtool.models import UserProfile, Query, Topic, BookReview, BookLiked, BookCart, BookRating, BookItem, History

# Register your models here.

admin.site.register(UserProfile)
# admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(Query)
admin.site.register(Topic)
# admin.site.register(BookLiked)
admin.site.register(BookCart)
admin.site.register(BookRating)
admin.site.register(BookItem)
admin.site.register(History)
