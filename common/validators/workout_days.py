from django.core.exceptions import ValidationError

from common.constants.choices import WorkoutDay


VALID_WORKOUT_DAYS = {
    choice[0]
    for choice in WorkoutDay.choices
}


def validate_workout_days(value):
    if not isinstance(value, list):
        raise ValidationError(
            "Workout days must be a list."
        )

    invalid_days = [
        day
        for day in value
        if day not in VALID_WORKOUT_DAYS
    ]

    if invalid_days:
        raise ValidationError(
            f"Invalid workout days: {invalid_days}"
        )