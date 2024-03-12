from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length=200, null=True)
  password = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
class Author(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
    
class Categories(models.Model):
  name = models.CharField(max_length=30)

  
class Book(models.Model):
  title = models.CharField(max_length=50)
  cover = models.ImageField(upload_to="static/images/cover", height_field=None, width_field=None, max_length=None, default="")
  price = models.IntegerField()
  author = models.ManyToManyField(Author)
  categories = models.ManyToManyField(Categories)
  description = models.TextField(null=True, blank=True)
  media = models.FileField(null=True, blank=True)
  
  def __str__(self):
    return self.title
  

  

  
  