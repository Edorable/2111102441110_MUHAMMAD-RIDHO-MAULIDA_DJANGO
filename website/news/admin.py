from django.contrib import admin
from news.models import Category, Article

# Register your models here.

admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['judul', 'kategori', 'author']
    search_fields = ['judul']
admin.site.register(Article, ArticleAdmin)