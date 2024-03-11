from django.contrib import admin
from .models import User, Categories, Book
# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Book)