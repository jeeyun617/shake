# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'post_list', name='post_list'),
    url(r'^(?P<id>\d+)/$', 'post_detail', name='post_detail'),
    url(r'^(?P<id>\d+)/comments/new/$', 'comment_new', name='comment_new'),
    url(r'^(?P<id>\d+)/comments/(?P<comment_id>\d+)/edit/$', 'comment_edit', name='comment_edit'),
    url(r'^(?P<id>\d+)/comments/(?P<comment_id>\d+)/delete/$', 'comment_delete', name='comment_delete'),
)
