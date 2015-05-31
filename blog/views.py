# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post, Comment
from blog.forms import CommentForm


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'form': form,
    })


def comment_new(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, id=id)
            comment.save()
            return redirect('blog:post_detail', id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_edit(request, id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_delete(request, id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', id)
    return render(request, 'blog/comment_delete_confirm.html', {
        'comment': comment,
    })
