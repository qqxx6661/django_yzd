from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Mall(models.Model):
    owner = models.ForeignKey(User, related_name='malls_created')
    subject = models.ForeignKey(Subject, related_name='malls')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Category(models.Model):
    mall = models.ForeignKey(Mall, related_name='categorys')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
        
    def __str__(self):
        return self.title
