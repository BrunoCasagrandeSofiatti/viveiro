from atexit import register
from django.contrib import admin
from .models import *

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriAdmin(admin.ModelAdmin):
    pass