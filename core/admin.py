from django.contrib import admin

from .models import Autor , Categoria,Compra, Editora, Livro


class EditoraAdmin (admin.ModelAdmin):
    list_display = ("nome","site")

class LivroAdmin (admin.ModelAdmin):
    list_display = ("titulo","ISBN","quantidade","preco","categoria","editora")


admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Compra)
admin.site.register(Editora,EditoraAdmin)
admin.site.register(Livro,LivroAdmin)