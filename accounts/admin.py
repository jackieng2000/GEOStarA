from django.contrib import admin
from .models import UserProfile, Profile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.
    """
    list_display = ('user', 'Phone')
    list_filter = ('user',)
    search_fields = ('user__username', 'Phone')
    ordering = ('user__username',)
    fieldsets = (
        (None, {
            'fields': ('user', 'Phone')
        }),
    )

    def get_queryset(self, request):
        """
        Optimize queryset by selecting related user.
        """
        return super().get_queryset(request).select_related('user')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.
    """
    list_display = ('user', 'userGroup', 'activityDate')
    list_filter = ('userGroup', 'activityDate')
    search_fields = ('user__username', 'userGroup')
    date_hierarchy = 'activityDate'
    ordering = ('user__username',)
    fieldsets = (
        (None, {
            'fields': ('user', 'userGroup', 'activityDate')
        }),
    )

    def get_queryset(self, request):
        """
        Optimize queryset by selecting related user.
        """
        return super().get_queryset(request).select_related('user')

# Register your models here.
