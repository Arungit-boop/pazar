from django.contrib import admin
from .models import Category, Blog, BlogComment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'admin_photo', 'timestamp',]
    list_filter = ['category',]
    search_fields = ['title', 'category',]

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'post', 'admin_photo', 'timestamp',]
admin.site.register((Category))
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)