from django.contrib import admin
from .models import GPSLocation, GPSLatest
from django.utils import timezone


@admin.register(GPSLatest)
class GPSLatestAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp', 'altitude', 'accuracy')
    list_filter = ('timestamp',)
    search_fields = ('user__username',)
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

# Optionally, register GPSLocation if not already registered
# @admin.register(GPSLocation)
# class GPSLocationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'timestamp', 'latitude', 'longitude', 'altitude', 'accuracy')
#     list_filter = ('timestamp', 'user')
#     search_fields = ('user__username',)
#     readonly_fields = ('timestamp',)
#     ordering = ('-timestamp',)

@admin.register(GPSLocation)
class GPSLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'formatted_timestamp', 'latitude', 'longitude', 'altitude', 'accuracy')
    list_filter = ('timestamp', 'user')
    search_fields = ('user__username',)
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

    def formatted_timestamp(self, obj):
        return timezone.localtime(obj.timestamp).strftime('%Y-%m-%d %H:%M:%S')
    formatted_timestamp.short_description = 'Timestamp'
    formatted_timestamp.admin_order_field = 'timestamp'


# @admin.register(GPSLocation)
# class GPSLocationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'latitude', 'longitude', 'formatted_timestamp', 'altitude', 'accuracy')
#     list_filter = ('timestamp', 'user')
#     search_fields = ('user__username',)
#     readonly_fields = ('timestamp',)
#     ordering = ('-timestamp',)

#     def formatted_timestamp(self, obj):
#         return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
#     formatted_timestamp.short_description = 'Timestamp'
#     formatted_timestamp.admin_order_field = 'timestamp'  # Allows sorting by timestamp