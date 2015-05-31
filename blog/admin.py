# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at']

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
