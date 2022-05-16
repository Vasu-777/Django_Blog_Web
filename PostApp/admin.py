from django.contrib import admin
from .models import Post,Comment,Like
# from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(admin.ModelAdmin):
    list_display =('title','author','date_posted','category','is_published')
    list_display_links=('title','author')
    list_order_by = ('-date_posted',)
    list_filter = ('category',)
    list_editable=('is_published',)
    # summernote_fields = ('content',)
    
# Register your models here.
admin.site.register(Post,PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user',  'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Like)        