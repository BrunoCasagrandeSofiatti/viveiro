from django.urls import path
from .views import *

urlpatterns = [
    path('produtos', ViewProdutos.as_view(), name='produtos'),
    path('selectcategoria/', ViewCategoria.as_view()),
    path('listarprodutos/', ViewProdutos.get_table),
]