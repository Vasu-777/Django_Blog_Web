from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'category_slug':('category_name',)}

admin.site.register(Category, CategoryAdmin)