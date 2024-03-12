from django.contrib import admin
from .models import User, Categories, Book, Author
# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Book)