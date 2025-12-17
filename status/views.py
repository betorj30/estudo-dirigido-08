from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Status
from .serializers import StatusSerializer
from drf_spectacular.utils import extend_schema
@extend_schema(
    tags=["Status"],
    summary="Lista e cria status",
    description="Endpoint para listagem e criação de status."
)

# Create your views here.
class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_permissions(self): 
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
    

    class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Status.objects.all()
        serializer_class = StatusSerializer
        permission_classes = [IsAuthenticated]