from rest_framework import serializers

from .models import Cultivo


class CultivoSerializer(serializers.ModelSerializer):
    """
    Convierte un Cultivo en JSON.
    - agricultor: se envía y se recibe como id (ForeignKey).
    - agricultor_nombre: solo lectura, para mostrar el nombre en el cliente.
    """

    agricultor_nombre = serializers.CharField(source="agricultor.nombre", read_only=True)

    class Meta:
        model = Cultivo
        fields = [
            "id",
            "nombre",
            "tipo",
            "cantidad_kg",
            "disponible_intercambio",
            "agricultor",
            "agricultor_nombre",
            "creado",
        ]
        read_only_fields = ["id", "creado"]

    def validate_cantidad_kg(self, valor):
        if valor <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor que 0.")
        return valor
