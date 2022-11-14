from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
