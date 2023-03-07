from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    last_modified = models.DateTimeField(auto_now=True)
    # mot bai viet nhieu binh luan
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=20)
    body = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)