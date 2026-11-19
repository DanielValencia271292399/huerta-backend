from django.contrib import admin

from .models import Cultivo


@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "tipo", "cantidad_kg", "disponible_intercambio", "agricultor")
    list_filter = ("tipo", "disponible_intercambio")
    search_fields = ("nombre",)
