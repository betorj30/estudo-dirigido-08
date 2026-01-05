from django.urls import path
from .views import (
    UnidadeListCreate,
    UnidadeDetail,
    SalaListCreate,
    SalaDetail,
    StatusListCreate,
    StatusDetail,   
    BemListCreate,
    BemDetail,
    CategoriaListCreate,
    CategoriaDetail,
    api_login,
)

urlpatterns = [
    path('unidades/', UnidadeListCreate.as_view()),
    path('unidades/<int:pk>/', UnidadeDetail.as_view()),
    path('salas/', SalaListCreate.as_view()),
    path('salas/<int:pk>/', SalaDetail.as_view()),
    path('status/', StatusListCreate.as_view()),
    path('status/<int:pk>/', StatusDetail.as_view()),
    path('bens/', BemListCreate.as_view()),
    path('bens/<int:pk>/', BemDetail.as_view()),
    path('categorias/', CategoriaListCreate.as_view()),
    path('categorias/<int:pk>/', CategoriaDetail.as_view()),
    path("login/", api_login),
]
