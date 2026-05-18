from rest_framework import serializers

from .models import (
    Exercise,
    ExercisePerformance,
    SharedWorkoutPlan,
)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class SharedWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedWorkoutPlan
        fields = "__all__"


class ExercisePerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePerformance
        fields = "__all__"