
from numpy import source
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Autor, Categoria, Editora, Livro, Compra, ItensCompra



class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class ItensDeCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro','quantidade')
        depth = 1

class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    status = SerializerMethodField()
    itens = ItensDeCompraSerializer(many=True)


    class Meta:
        model = Compra
        fields = '__all__'

    def get_status(self, instance):
        return instance.get_status_display()


