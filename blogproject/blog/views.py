# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from comments.forms import CommentForm
def index(request):
    #post_list = Post.objects.all().order_by('-created_time')
    post_list = Post.objects.all() # 已经在Post中设置内置类Meta中设置了ordering,此处不需要order_by了.
    return render(request, 'blog/index.html', context={'post_list' : post_list})


def detail(request, pk):
    #从 django.shortcuts 模块导入的 get_object_or_404 方法,
    # 其作用就是当传入的 pk 对应的 Post 在数据库存在时,就返回对应的 post,
    # 如果不存在,就给用户返回一个 404 错误，表明用户请求的文章不存在.
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()
    comment_count = post.comment_set.count()
    return render(request, 'blog/detail.html', context={'post':post,
                                                        'form':form,
                                                        'comment_list':comment_list,
							'comment_count':comment_count
							})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
				    created_time__month=month
				    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def category(request, pk):
    #error: cate = get_object_or_404(Category, pk),which will except a errot : 'need more than 1 value to unpack python'
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})
# Create your views here.
