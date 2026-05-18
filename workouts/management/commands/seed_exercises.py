from django.core.management.base import BaseCommand

from workouts.models import Exercise
from workouts.seed_data.exercises import EXERCISES


class Command(BaseCommand):
    help = "Seed exercise database"

    def handle(self, *args, **kwargs):
        created_count = 0
        updated_count = 0

        for exercise_data in EXERCISES:
            _, created = Exercise.objects.update_or_create(
                name=exercise_data["name"],
                defaults=exercise_data,
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Exercises seeded successfully. "
                f"Created: {created_count}, "
                f"Updated: {updated_count}"
            )
        )