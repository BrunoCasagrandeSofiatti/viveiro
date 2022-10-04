from django.urls import path
from .views import *

urlpatterns = [
    # Produtos
    path('produtos', ViewProdutos.as_view(), name='produtos'),
    path('selectcategoria/', ViewCategoria.get_select),
    path('listarprodutos/', ViewProdutos.get_table),
    path('deletarprodutos/', delete_prod),

    # Categorias
    path('categorias', ViewCategoria.as_view(), name='categorias'),
    path('listarcategorias/', ViewCategoria.get_table),

    # Estoque
    path('estoque', ViewEstoque.as_view(), name='estoque'),
]