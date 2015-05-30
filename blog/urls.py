# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'post_list', name = 'post_list'),
    url(r'^(?P<id>\d+)/$', 'post_detail', name = 'post_detail'),
)
