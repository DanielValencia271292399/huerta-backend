from django.db import models


class Agricultor(models.Model):
    """Vecino que participa en la huerta comunitaria."""

    nombre = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "agricultor"
        verbose_name_plural = "agricultores"

    def __str__(self):
        return self.nombre
