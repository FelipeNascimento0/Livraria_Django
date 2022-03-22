

from core.views import teste, CategoriaView, CategoriaList, CategoriaDetail, CategoriasListGeneric, CategoriaUpdateDestroy, CategoriasViewSet
from django.urls import path, include


from core.views.editora import EditoraViewSet
from core.views.autor import AutorViewSet
from core.views.livro import LivroViewSet
from core.views.compra import CompraViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorias', CategoriasViewSet, basename='categoria')
router.register('editora', EditoraViewSet, basename="editora")
router.register('autor', AutorViewSet, basename="autor")
router.register('livro', LivroViewSet, basename='livro')
router.register('compra', CompraViewSet, basename='compra')


urlpatterns = [
    path('', teste),
    path('categorias-class/', CategoriaView.as_view()),
    path('categorias-class/<int:id>/', CategoriaView.as_view()),
    path('categorias-apiview/', CategoriaList.as_view()),
    path('categorias-apiview/<int:id>/',CategoriaDetail.as_view()),
    path('categorias-generic/', CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', CategoriaUpdateDestroy.as_view()),
    path('', include(router.urls)),
]