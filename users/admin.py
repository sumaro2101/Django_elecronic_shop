from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name', 'password')
    search_fields = ('username', 'first_name', 'last_name', 'email')