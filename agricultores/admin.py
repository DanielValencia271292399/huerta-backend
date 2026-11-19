from django.contrib import admin

from .models import Agricultor


@admin.register(Agricultor)
class AgricultorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "barrio", "telefono")
    search_fields = ("nombre", "barrio")
