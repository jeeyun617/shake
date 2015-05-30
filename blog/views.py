# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
    })


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })