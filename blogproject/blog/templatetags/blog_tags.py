# -*- coding: utf-8 -*-
from django import template
from ..models import Post, Category

register = template.Library()

#最新文章模板标签
    #按照 Django 的规定注册这个函数为模板标签.
    #能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    # not Category.objects().all()(which will except a error :'Manager' object is not callable ), is Category.objects.all(), 
    return Category.objects.all()
