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


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class SharedWorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = SharedWorkoutPlan.objects.all()
    serializer_class = SharedWorkoutPlanSerializer


class ExercisePerformanceViewSet(viewsets.ModelViewSet):
    queryset = ExercisePerformance.objects.all()
    serializer_class = ExercisePerformanceSerializer