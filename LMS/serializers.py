from rest_framework import serializers
from .models import User, Book, Author, Categories
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password', 'groups']
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name',)
    
class BookSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  class Meta:
    model = Book
    fields = '__all__'

    
