from rest_framework.viewsets import ModelViewSet

from core.serializer import CategoriaSerializer
from core.models import Categoria

class CategoriasViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer