from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Cada app registra sus rutas con un router de DRF
    path("api/", include("agricultores.urls")),
    path("api/", include("cultivos.urls")),
]
