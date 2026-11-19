from rest_framework.routers import SimpleRouter

from .views import AgricultorViewSet

router = SimpleRouter()
router.register("agricultores", AgricultorViewSet, basename="agricultor")

urlpatterns = router.urls
