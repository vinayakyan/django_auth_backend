from django.contrib import admin
from .models import Tags, Blog, Comments


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_by', 'created_time')


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'comment_by', 'comment_time')

