from rest_framework import viewsets

from .models import Agricultor
from .serializers import AgricultorSerializer


class AgricultorViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de agricultores:
    GET /api/agricultores/          -> listar
    POST /api/agricultores/         -> crear
    GET /api/agricultores/{id}/     -> detalle
    PUT/PATCH /api/agricultores/{id}/ -> editar
    DELETE /api/agricultores/{id}/  -> eliminar
    """

    queryset = Agricultor.objects.all().order_by("nombre")
    serializer_class = AgricultorSerializer
