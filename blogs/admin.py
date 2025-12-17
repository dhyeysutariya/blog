from django.contrib import admin

from blogs.models import Blog, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','created_at','updated_at')

admin.site.register(Category,CategoryAdmin)
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('title','slug','short_description','category','is_featured','status')
    search_fields=('title','slug','short_description','category__category_name','status')
    prepopulated_fields={'slug':('title',)}
    list_editable=('is_featured',)

admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('user','blog','comment')

admin.site.register(Comment,CommentAdmin)