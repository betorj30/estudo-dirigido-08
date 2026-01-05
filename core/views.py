from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .models import Unidades, Salas, Status, Bem, Categoria
from .serializers import (
    UnidadeSerializer,
    SalaSerializer,
    StatusSerializer,
    BemSerializer,
    CategoriaSerializer,
)

# importações para autenticação
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# codigo estudo dirigido 8 e hand on
def home(request):
    return HttpResponse("Bem-vindo ao sistema de inventário de bens!")

class UnidadeListCreate(generics.ListCreateAPIView):
    queryset = Unidades.objects.all()
    serializer_class = UnidadeSerializer

class UnidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidades.objects.all()
    serializer_class = UnidadeSerializer


class SalaListCreate(generics.ListCreateAPIView):
    queryset = Salas.objects.all()
    serializer_class = SalaSerializer

class SalaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salas.objects.all()
    serializer_class = SalaSerializer


class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class BemListCreate(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# codigo estudo dirigido 9

@api_view(["POST"])
@permission_classes([AllowAny])

def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse({"detail": "Credenciais inválidas"}, status=4)
    
    login(request, user)
    return JsonResponse({"detail": "Login realizado com sucesso"})


