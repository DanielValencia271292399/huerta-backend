from rest_framework import serializers

from .models import Agricultor


class AgricultorSerializer(serializers.ModelSerializer):
    """Convierte un Agricultor en JSON y valida el JSON que llega para crearlo o editarlo."""

    class Meta:
        model = Agricultor
        fields = ["id", "nombre", "barrio", "telefono", "creado"]
        read_only_fields = ["id", "creado"]
