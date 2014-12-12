from django.contrib import admin

from .models import Community


class CommunityAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['title', 'status', 'created_at', 'updated_at']
    search_fields = ['title']


admin.site.register(Community, CommunityAdmin)