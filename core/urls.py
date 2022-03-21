

from core.views import teste, CategoriaView, CategoriaList, CategoriaDetail, CategoriasListGeneric, CategoriaUpdateDestroy, CategoriasViewSet
from django.urls import path, include


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorias-viewset', CategoriasViewSet, basename='user')


urlpatterns = [
    path('', teste),
    path('categorias/', CategoriaView.as_view()),
    path('categorias/<int:id>/', CategoriaView.as_view()),
    path('categorias-apiview/', CategoriaList.as_view()),
    path('categorias-apiview/<int:id>/',CategoriaDetail.as_view()),
    path('categorias-generic/', CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', CategoriaUpdateDestroy.as_view()),
    path('', include(router.urls)),
]