from django.contrib import admin
from suit.admin import SortableModelAdmin

from .models import Post, Category, Tag, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage


class PostAdmin(SortableModelAdmin):
    list_per_page = 10
    list_display = ['title', 'category', 'active', 'ordering', 'created_at', 'updated_at']
    search_fields = ['title', 'body', 'ordering', 'category__title']
    list_filter = ['category', 'tags', 'active']
    filter_horizontal = ['tags']
    sortable = 'ordering'

    inlines = [PostImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['title', 'active', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['active']


class TagAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['title', 'active', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['active']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)