from django.contrib import admin
from blog.models import Category, Post, Comment

# Register your models here.
admin.site.register([Category, Post, Comment])
