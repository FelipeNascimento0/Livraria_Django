
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.serializer import CategoriaSerializer
from core.models import Categoria



class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaUpdateDestroy(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer