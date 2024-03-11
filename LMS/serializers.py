from rest_framework import serializers
from .models import User, Book, Author, Categories

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password']
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name')
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('name')
    
class BookSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  class Meta:
    model = Book
    fields = '__all__'

    
