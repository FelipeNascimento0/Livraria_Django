

from core import views
from django.urls import path, include


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorias-viewset', views.CategoriasViewSet, basename='user')


urlpatterns = [
    path('', views.teste),
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:id>/', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriaList.as_view()),
    path('categorias-apiview/<int:id>/', views.CategoriaDetail.as_view()),
    path('categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', views.CategoriaUpdateDestroy.as_view()),
    path('', include(router.urls)),
]