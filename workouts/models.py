from django.conf import settings
from django.db import models

from buddy.models import BuddyPair
from gyms.models import Gym

from common.constants.choices import (
    FitnessLevel,
    EquipmentType,
    MovementPattern,
    MuscleGroup,
    WorkoutSplit,
)
from django.core.validators import MinValueValidator
from common.models.base import TimeStampedModel
from common.validators.injury_tags import (
    validate_injury_tags,
)


class Exercise(TimeStampedModel):
    name = models.CharField(max_length=255)

    primary_muscle = models.CharField(
        max_length=50,
        choices=MuscleGroup.choices,
    )

    secondary_muscles = models.JSONField(
        default=list,
    )

    equipment_type = models.CharField(
        max_length=50,
        choices=EquipmentType.choices,
    )

    movement_pattern = models.CharField(
        max_length=50,
        choices=MovementPattern.choices,
    )

    injury_risk = models.JSONField(
        default=dict,
        help_text="Joint risk mapping",
    )

    movement_tags = models.JSONField(
        default=list,
        validators=[validate_injury_tags],
    )

    difficulty = models.CharField(
        max_length=20,
        choices=FitnessLevel.choices,
    )

    unilateral_or_bilateral = models.CharField(
        max_length=20,
    )

    estimated_station_time_minutes = models.PositiveIntegerField()

    default_sets = models.PositiveIntegerField()

    default_rep_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SharedWorkoutPlan(TimeStampedModel):
    buddy_pair = models.ForeignKey(
        BuddyPair,
        on_delete=models.CASCADE,
        related_name="workout_plans",
    )

    selected_gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="workout_plans",
    )

    recommended_split = models.CharField(
        max_length=50,
        choices=WorkoutSplit.choices,
    )

    shared_days = models.JSONField(default=list)

    plan_json = models.JSONField(default=dict)

    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Workout Plan #{self.id}"


class ExercisePerformance(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exercise_performances",
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="performances",
    )

    workout_plan = models.ForeignKey(
        SharedWorkoutPlan,
        on_delete=models.CASCADE,
        related_name="performances",
    )

    performed_weight = models.FloatField(
        validators=[MinValueValidator(0)],
    )

    performed_reps = models.PositiveIntegerField()

    rir = models.PositiveIntegerField(
        help_text="Reps in reserve",
    )

    performed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name}"