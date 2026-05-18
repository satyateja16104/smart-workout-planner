from rest_framework.routers import DefaultRouter

from .views import (
    InjuryRecordViewSet,
    UserProfileViewSet,
)

router = DefaultRouter()

router.register(
    r"profiles",
    UserProfileViewSet,
    basename="profiles",
)

router.register(
    r"injuries",
    InjuryRecordViewSet,
    basename="injuries",
)

urlpatterns = router.urls