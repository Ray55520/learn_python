# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __unicode__(self):
        return self.text[:20]
# Create your models here.
