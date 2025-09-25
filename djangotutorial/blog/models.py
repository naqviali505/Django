from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    content = models.TextField()

    def __str__(self):
        return self.content


class BlogCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name='Blog Category')

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(BlogCategory)
    comments = models.ManyToManyField(Comment,blank=True)

    def __str__(self):
        return self.title

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','user','categories', 'comments']


class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','user']