from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'mini_descr', 'full_descr')
    list_editable = ('price',)