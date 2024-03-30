from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your models here.
class Category(models.Model):
    name = models.CharField('Categories', max_length = 50)
    slug = models.SlugField(max_length = 50)
    
    def __str__(self):
	    return self.name
   

class Book(models.Model):
    title = models.CharField(max_length= 100)
    slug = models.SlugField(max_length =100)
    author = models.CharField(max_length = 50)
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to ='pdf')
    selfdev_books = models.BooleanField(default=False)
    biography_books = models.BooleanField(default=False)
    academic_books = models.BooleanField(default=False)
    
    def __str__(self):
	    return self.title

class BookSearch(models.Model):
    name_of_book = models.CharField(max_length = 100)

    def __str__(self):
	    return self.name_of_book

class Categoryp(models.Model):
    name = models.CharField('Categoriesp', max_length = 50)
    slug = models.SlugField(max_length = 50)
    
    def __str__(self):
	    return self.name
   

class PremiumBook(models.Model):
    title = models.CharField(max_length= 100)
    slug = models.SlugField(max_length =100)
    categoryp = models.ManyToManyField(Categoryp, related_name='books')
    pdf = models.FileField(upload_to ='pdf')
    junior_books = models.BooleanField(default=False)
    senior_books = models.BooleanField(default=False)
    lower_books = models.BooleanField(default=False)
    
    def __str__(self):
	    return self.title



class AllUsers(models.Model):
    username =models.CharField(max_length = 100)
    password =models.CharField(max_length = 100)

class Users(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
   
    
class MyUsers(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    usertype = models.CharField(max_length = 100)




      
     