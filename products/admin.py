from django.contrib import admin

from .models import Category, File, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_enable', 'update_time')
    list_filter = ('is_enable',)
    search_fields = ('title',)


class FileInline(admin.TabularInline):
    model = File
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_enable', 'update_time')
    list_filter = ('is_enable', 'categories')
    search_fields = ('title',)
    inlines = [FileInline]
