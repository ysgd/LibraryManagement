from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import User,Book,Author,Categories
from .serializers import UserSerializer, BookSerializer, AuthorSerializer,CategorySerializer, GroupSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group

# Create your views here.
# def home(request):
#   return render(request, "index.html")

# def categories(request):
#   return render(request, "categories.html")


class GroupView(ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [AllowAny]

class CategoryViewSet(ModelViewSet):
  queryset = Categories.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [AllowAny]

class AuthorViewSet(ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  permission_classes = [AllowAny]

class AddBook(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  search_fields = ['title']
  permission_classes = [AllowAny]


class UserView(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
  
  def register(self,request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      password = request.data.get('password')
      hash_password = make_password(password)
      a = serializer.save()
      a.password = hash_password
      a.save()
      return Response("user created")
    else:
      return Response(serializer.errors)
    
  def login(self,request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username=email,password=password)
    
    if user == None:
      return Response('invalid credentials!')
    else:
      token,_ = Token.objects.get_or_create(user=user)
      return Response(token.key)
  