from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length=200, null=True)
  password = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
class Book(models.Model):
  title = models.CharField(max_length=50)
  price = models.IntegerField()
  author = models.CharField(max_length=50)
  description = models.TextField()
  

  
  