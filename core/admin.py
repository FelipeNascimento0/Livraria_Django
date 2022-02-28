from django.contrib import admin

from .models import Categoria, Editora


class EditoraAdmin (admin.ModelAdmin):
    list_display = ("nome","site")

admin.site.register(Categoria)
admin.site.register(Editora,EditoraAdmin)