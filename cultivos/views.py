from rest_framework import viewsets

from .models import Cultivo
from .serializers import CultivoSerializer


class CultivoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de cultivos:
    GET /api/cultivos/          -> listar
    POST /api/cultivos/         -> crear
    GET /api/cultivos/{id}/     -> detalle
    PUT/PATCH /api/cultivos/{id}/ -> editar
    DELETE /api/cultivos/{id}/  -> eliminar
    """

    # select_related trae el agricultor en la misma consulta SQL
    queryset = Cultivo.objects.select_related("agricultor").all()
    serializer_class = CultivoSerializer
