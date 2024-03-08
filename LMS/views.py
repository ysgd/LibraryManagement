from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import User,Book
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

# Create your views here.
def home(request):
  return render(request, "index.html")


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
  