from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'full_name', 'is_active', 'is_staff', 'date_joined', 'profile_picture')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'full_name')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        ("User Info", {'fields': ('email', 'full_name', 'password')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ("Important Dates", {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        ("Create New User", {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2')}
         ),
    )

    def profile_picture(self, obj):
        if hasattr(obj, 'profile') and obj.profile.image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                               obj.profile.image.url)
        return "No Image"

    profile_picture.short_description = "Profile Picture"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_preview', 'bio')
    search_fields = ('user__email', 'user__full_name')
    readonly_fields = ('image_preview',)

    fieldsets = (
        ("User Profile", {'fields': ('user', 'bio', 'image', 'image_preview')}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="80" style="border-radius:50%;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"
