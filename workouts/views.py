from rest_framework import viewsets

from .models import (
    Exercise,
    ExercisePerformance,
    SharedWorkoutPlan,
)

from .serializers import (
    ExercisePerformanceSerializer,
    ExerciseSerializer,
    SharedWorkoutPlanSerializer,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SharedWorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = SharedWorkoutPlan.objects.all()
    serializer_class = SharedWorkoutPlanSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        "filter to only plans where the user is the creator or it's shared with them"
        return SharedWorkoutPlan.objects.filter(
        buddy_pair__host=self.request.user
    ) | SharedWorkoutPlan.objects.filter(
        buddy_pair__join=self.request.user
    )

class ExercisePerformanceViewSet(viewsets.ModelViewSet):
    queryset = ExercisePerformance.objects.all()
    serializer_class = ExercisePerformanceSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        "filter to only performances where the user is the one who performed it"
        return ExercisePerformance.objects.filter(user=self.request.user)