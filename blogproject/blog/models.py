# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        #它的第一个参数的值是 'blog:detail',意思是 blog 应用下的 name=detail 的函数.
        return reverse('blog:detail', kwargs={'pk' : self.pk})

    class Meta:
        ordering = ['-created_time']
	#ordering 属性用来指定文章排序方式,['-created_time'] 指定了依据哪个属性的值进行排序,这里指定为按照文章发布时间排序,且负号表示逆序排列.
# Create your models here.
