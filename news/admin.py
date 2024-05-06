from django.contrib import admin
from .models import Posts, PostComment
# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'name_user', 'image', 'slug', 'views', 'likes', 'time_published', 'time_edit', 'is_edit', 'text_to_edit', 'comment_count', 'name_button')
    search_fields = ('pk', 'title', 'name_user', 'time_published')
    list_filter = 'is_edit',
    
    prepopulated_fields = {'slug': ('name_user', 'title')}
    
@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'user_name', 'image', 'text', 'time_published', 'time_edit', 'is_edit', 'text_to_edit', 'text_to_post', 'likes')
    search_fields = ('post', 'user_name', 'time_published')
    list_filter = 'is_edit',
    