from json import JSONEncoder
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .models import *

class ViewProdutos(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'produtos.html')  

    def get_table(self):
        prod = Produto.objects.all().values('descricao','categoria__descricao', 'data_cadastro').order_by('descricao')
        response = []
        for i in prod:
            obj = {
                "descricao": i['descricao'],
                "categoria": i['categoria__descricao'],
                "data_cadastro": i['data_cadastro'],
                "acoes": "teste"
            }
            response.append(obj)

        return JsonResponse(response, status=200, safe=False)


class ViewCategoria(View):
    def get(self, request, *args, **kwargs):
        cat = Categoria.objects.all().values('id','descricao').order_by('descricao')
        response = []
        for i in cat:
            response += [{'id': i['id'], 'descricao': i['descricao']}]

        return JsonResponse(response, status=200, safe=False)