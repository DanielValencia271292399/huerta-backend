from rest_framework.routers import SimpleRouter

from .views import CultivoViewSet

router = SimpleRouter()
router.register("cultivos", CultivoViewSet, basename="cultivo")

urlpatterns = router.urls
