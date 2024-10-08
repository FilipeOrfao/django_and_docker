from django.contrib import admin
from blog.models import Category, Post, Comment

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register([Category, Post, Comment])
