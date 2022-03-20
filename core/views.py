from dataclasses import fields
from unicodedata import category
from urllib import request, response
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response


from core.models import Categoria
import json





def teste(request):
    return HttpResponse("Olá pessoal do GitHub")



#=======================================================================#
#=====================FAZENDO AS REQUISIÇÕES COM JSON===================#
#=======================================================================#

@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id = id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json") 

    def post(self,request):
        
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id = id)
        qs.descricao = json_data['descricao']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Categoria.objects.get(id = id)
        qs.delete()
        data = {'mensagem': 'item exluido com sucesso'}
        return JsonResponse(data)

#=======================================================================-#



#=======================================================================#
#=================FAZENDO AS REQUISIÇÕES COM API REST===================#
#=======================================================================#



'''Aqui fiz um teste com varias maneiras de realizar um CRUD -----------'''

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriaList(APIView):
    
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetail(APIView):
        def get(self,request, id):
            categoria = get_object_or_404(Categoria.objects.all(), id=id)
            serializer = CategoriaSerializer(categoria)
            return Response(serializer.data)

        def put(self,request, id):
            categoria = get_object_or_404(Categoria.objects.all(), id=id)
            serializer = CategoriaSerializer(categoria)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, id):
            categoria = get_object_or_404(Categoria.objects.all, id=id)
            categoria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



#=======================================================================#
#=====================USANDO GENERIC VIEWS DO REST_FRAMEWORK============#
#=======================================================================#


class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaUpdateDestroy(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#=======================================================================#
#=====================USANDO VIEWSET DO REST_FRAMEWORK==================#
#=======================================================================#


class CategoriasViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

            
            