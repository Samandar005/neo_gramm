from django.contrib import admin
from .models import Comments

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('short_comment', 'post_caption', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('comments', 'user__full_name', 'posts__caption')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    def short_comment(self, obj):
        return obj.comments[:50] + "..." if len(obj.comments) > 50 else obj.comments
    short_comment.short_description = "Comment"

    def post_caption(self, obj):
        return obj.posts.caption
    post_caption.short_description = "Post"
