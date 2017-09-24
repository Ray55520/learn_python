# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Post, Category, Tag
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# Register your models here.
