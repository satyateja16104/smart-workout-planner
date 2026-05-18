from rest_framework.routers import DefaultRouter

from .views import (
    ExercisePerformanceViewSet,
    ExerciseViewSet,
    SharedWorkoutPlanViewSet,
)

router = DefaultRouter()

router.register(
    r"exercises",
    ExerciseViewSet,
    basename="exercises",
)

router.register(
    r"plans",
    SharedWorkoutPlanViewSet,
    basename="plans",
)

router.register(
    r"performances",
    ExercisePerformanceViewSet,
    basename="performances",
)

urlpatterns = router.urls