from django.db import models

from agricultores.models import Agricultor


class Cultivo(models.Model):
    """Semilla o cosecha que un agricultor ofrece en la huerta."""

    TIPOS = [
        ("hortaliza", "Hortaliza"),
        ("fruta", "Fruta"),
        ("aromatica", "Aromática"),
        ("grano", "Grano"),
        ("semilla", "Semilla"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS, default="hortaliza")
    cantidad_kg = models.DecimalField(max_digits=7, decimal_places=2)
    disponible_intercambio = models.BooleanField(default=True)
    # Relación: muchos cultivos pertenecen a un agricultor
    agricultor = models.ForeignKey(
        Agricultor,
        on_delete=models.CASCADE,
        related_name="cultivos",
    )
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return f"{self.nombre} ({self.agricultor})"
