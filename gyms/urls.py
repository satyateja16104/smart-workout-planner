from rest_framework.routers import DefaultRouter

from .views import (
    GymEquipmentViewSet,
    GymViewSet,
)

router = DefaultRouter()

router.register(
    r"gyms",
    GymViewSet,
    basename="gyms",
)

router.register(
    r"equipment",
    GymEquipmentViewSet,
    basename="equipment",
)

urlpatterns = router.urls