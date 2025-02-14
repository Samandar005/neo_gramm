from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('caption', 'author', 'likes_count', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('caption', 'hashtags', 'author__full_name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Likes"
