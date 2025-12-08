from rest_framework import serializers
from .models import Unidades, Salas, Status, Bem, Categoria

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidades
        fields = "__all__"

class SalaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Salas
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class BemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bem
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"