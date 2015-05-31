# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from blog.utils import random_name_upload_to


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to=random_name_upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    photo = models.ImageField(upload_to=random_name_upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
