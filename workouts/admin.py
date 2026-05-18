from django.contrib import admin

from .models import (
    Exercise,
    ExercisePerformance,
    SharedWorkoutPlan,
)


admin.site.register(Exercise)
admin.site.register(SharedWorkoutPlan)
admin.site.register(ExercisePerformance)