from django.contrib import admin

from AppBlog.models import Post

# Register your models here.

# Se agrega en Panel Administrador visualizar los campos titulo, autor y fecha, 
# poder buscar registros con estos campos y filtrar por fecha.

class PostAdmin(admin.ModelAdmin):
    list_display=("raza","autor","fecha")
    search_fields=("raza","autor","fecha")
    list_filter= ("fecha",)
    date_hierarchy="fecha"

admin.site.register(Post, PostAdmin)