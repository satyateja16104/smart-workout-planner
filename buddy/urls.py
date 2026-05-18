from rest_framework.routers import DefaultRouter

from .views import BuddyPairViewSet

router = DefaultRouter()

router.register(
    r"pairs",
    BuddyPairViewSet,
    basename="pairs",
)

urlpatterns = router.urls