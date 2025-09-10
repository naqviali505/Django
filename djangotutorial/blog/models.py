from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs',null=True)

    def __str__(self):
        return self.title

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogs',null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users',null=True)
    content = models.TextField()

    def __str__(self):
        return self.content

