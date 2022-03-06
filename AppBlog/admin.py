from django.contrib import admin

from AppBlog.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=("titulo","autor","fecha")
    search_fields=("titulo","autor","fecha")

admin.site.register(Blog, BlogAdmin)