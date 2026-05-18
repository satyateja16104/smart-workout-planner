from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from common.constants.choices import (
    FitnessGoal,
    FitnessLevel,
    InjurySeverity,
    WorkoutDay,
)
from common.models.base import TimeStampedModel
from common.validators.workout_days import (
    validate_workout_days,
)
from common.validators.injury_tags import (
    validate_injury_tags,
)

class User(AbstractUser):
    """
    Custom user model for future extensibility.
    """
    pass


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    goal = models.CharField(
        max_length=50,
        choices=FitnessGoal.choices,
    )

    fitness_level = models.CharField(
        max_length=20,
        choices=FitnessLevel.choices,
    )

    preferred_workout_days = models.JSONField(
        default=list,
        validators=[validate_workout_days],
        help_text="List of workout days",
    )

    preferred_session_duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} Profile"


class InjuryRecord(TimeStampedModel):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="injuries",
    )

    joint = models.CharField(max_length=100)

    severity = models.CharField(
        max_length=20,
        choices=InjurySeverity.choices,
    )

    banned_movement_tags = models.JSONField(
        default=list,
        validators=[validate_injury_tags],
        help_text="List of restricted movement tags",
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - {self.joint}"