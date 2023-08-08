from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category_id']
    list_display_links = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'active_offer', 'category_id', 'subcategory_id']
    list_display_links = ['title', 'slug', 'price']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'time_creation', 'time_update', 'username_id']
