from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Product
import shop.translation

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug_en': ('name_en',), 'slug_es': ('name_es',)}

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'available',
        'created',
        'updated',
    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug_en': ('name_en',), 'slug_es': ('name_es',)}