import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

class ViewProdutos(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'produtos.html')  

    def get_table(self):
        prod = Produto.objects.all().values('id','descricao','categoria__descricao', 'data_cadastro').order_by('descricao')
        response = []
        for i in prod:
            obj = {                
                "descricao": i['descricao'],
                "categoria": i['categoria__descricao'],
                "data_cadastro": i['data_cadastro'],
                "id": i['id'],
            }
            response.append(obj)

        return JsonResponse(response, status=200, safe=False)

    def post(self, request, *args, **kwargs):
        # Recupera os valores enviados via ajax
        desc = request.POST['produto_name']
        cat_id = request.POST['categoria_id']
        dt_cadastro = request.POST['data_cadastro']

        # Verificar se tem algum produto ja cadastrado com o mesmo nome
        verprod = Produto.objects.filter(descricao= desc).first()
        if verprod:
            data = {'message': f'O produto: {verprod} já esta cadastrado!', 'type': 2}        
            return JsonResponse(data, status=200, safe=False)

        newprod = Produto(descricao = desc, categoria= Categoria.objects.get(id= cat_id), data_cadastro= dt_cadastro)
        newprod.save()
        data = {'message': f'Produto {desc} Salvo com Sucesso!', 'type': 1}
        
        return JsonResponse(data, status=200, safe=False)
    
@csrf_exempt
def delete_prod(request, *args, **kwargs):
    id_produto = request.POST['id_produto']
    try:
        prod = Produto.objects.get(id= id_produto)
        prod.delete()
        data = {'message': f'Produto {prod} Deletado com Sucesso!', 'type': 1}
        
        return JsonResponse(data, status=200, safe=False)
    except:
        data = {'message': f'Falha ao deletar produto!', 'type': 2}        
        return JsonResponse(data, status=200, safe=False)


    
class ViewEstoque(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'produtos.html')  


class ViewCategoria(View):
    def get_select(self):
        cat = Categoria.objects.all().values('id','descricao').order_by('descricao')
        response = []
        for i in cat:
            response += [{'id': i['id'], 'descricao': i['descricao']}]

        return JsonResponse(response, status=200, safe=False)

    def get(self, request, *args, **kwargs):
        return render(request, 'categorias.html')

    def get_table(self):
        category = Categoria.objects.all().values('id','descricao').order_by('descricao')
        response = []
        for i in category:
            obj = {                
                "descricao": i['descricao'],
                "id": i['id'],
            }
            response.append(obj)

        return JsonResponse(response, status=200, safe=False)

@csrf_exempt
def delete_cat(request, *args, **kwargs):
    id_category = request.POST['id_categoria']
    try:
        cat = Categoria.objects.get(id= id_category)
    except:
        data = {'message': f'Falha ao deletar Categoria!', 'type': 2}
    


    cat.delete()
    data = {'message': f'Produto {cat} Deletado com Sucesso!', 'type': 1}
    return JsonResponse(data, status=200, safe=False)