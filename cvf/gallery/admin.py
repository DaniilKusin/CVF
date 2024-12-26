from django.contrib import admin
from .models import UserImage

@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'uploaded_at', 'description')
    list_filter = ('uploaded_at',)
    search_fields = ('user__username', 'description')
