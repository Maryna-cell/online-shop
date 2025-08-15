from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')  # <-- Добавьте 'slug' сюда

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')  # <-- И сюда тоже

translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)