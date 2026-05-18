from django.db import models


class FitnessGoal(models.TextChoices):
    HYPERTROPHY = "hypertrophy", "Hypertrophy"
    STRENGTH = "strength", "Strength"
    FAT_LOSS = "fat_loss", "Fat Loss"
    GENERAL_FITNESS = "general_fitness", "General Fitness"
    ENDURANCE = "endurance", "Endurance"


class FitnessLevel(models.TextChoices):
    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    ADVANCED = "advanced", "Advanced"



class EquipmentType(models.TextChoices):
    BARBELL = "barbell", "Barbell"
    DUMBBELLS = "dumbbells", "Dumbbells"
    BENCH = "bench", "Bench"
    SQUAT_RACK = "squat_rack", "Squat Rack"
    SMITH_MACHINE = "smith_machine", "Smith Machine"
    CABLES = "cables", "Cables"
    PULLUP_BAR = "pullup_bar", "Pull-up Bar"
    MACHINE = "machine", "Machine"
    BODYWEIGHT = "bodyweight", "Bodyweight"
    KETTLEBELL = "kettlebell", "Kettlebell"
    CARDIO_MACHINE = "cardio_machine", "Cardio Machine"
    BANDS = "bands", "Bands"


class MuscleGroup(models.TextChoices):
    CHEST = "chest", "Chest"
    BACK = "back", "Back"
    SHOULDERS = "shoulders", "Shoulders"
    BICEPS = "biceps", "Biceps"
    TRICEPS = "triceps", "Triceps"
    FOREARMS = "forearms", "Forearms"
    LEGS = "legs", "Legs"
    GLUTES = "glutes", "Glutes"
    HAMSTRINGS = "hamstrings", "Hamstrings"
    CALVES = "calves", "Calves"
    CORE = "core", "Core"
    FULL_BODY = "full_body", "Full Body"
    CARDIO = "cardio", "Cardio"


class MovementPattern(models.TextChoices):
    HORIZONTAL_PUSH = "horizontal_push", "Horizontal Push"
    VERTICAL_PUSH = "vertical_push", "Vertical Push"
    HORIZONTAL_PULL = "horizontal_pull", "Horizontal Pull"
    VERTICAL_PULL = "vertical_pull", "Vertical Pull"
    SQUAT = "squat", "Squat"
    HIP_HINGE = "hip_hinge", "Hip Hinge"
    LUNGE = "lunge", "Lunge"
    CORE = "core", "Core"
    CARRY = "carry", "Carry"
    ROTATION = "rotation", "Rotation"
    CARDIO = "cardio", "Cardio"
    ISOLATION = "isolation", "Isolation"


class InjurySeverity(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"


class WorkoutSplit(models.TextChoices):
    FULL_BODY = "full_body", "Full Body"
    UPPER_LOWER = "upper_lower", "Upper Lower"
    PUSH_PULL_LEGS = "push_pull_legs", "Push Pull Legs"
    BRO_SPLIT = "bro_split", "Bro Split"
    HYBRID = "hybrid", "Hybrid"


class WorkoutDay(models.TextChoices):
    MONDAY = "monday", "Monday"
    TUESDAY = "tuesday", "Tuesday"
    WEDNESDAY = "wednesday", "Wednesday"
    THURSDAY = "thursday", "Thursday"
    FRIDAY = "friday", "Friday"
    SATURDAY = "saturday", "Saturday"
    SUNDAY = "sunday", "Sunday"


class BuddyPairStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    ACTIVE = "active", "Active"
    REJECTED = "rejected", "Rejected"