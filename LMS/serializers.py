from rest_framework import serializers
from .models import User, Book, Author, Category

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password']
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
    
class BookSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  class Meta:
    model = Book
    fields = '__all__'

    
