EXERCISES = [
    {
        "name": "Barbell Bench Press",
        "primary_muscle": "chest",
        "secondary_muscles": ["triceps", "shoulders"],
        "equipment_type": "barbell",
        "movement_pattern": "horizontal_push",
        "injury_risk": {
            "shoulder": "medium",
            "elbow": "low",
        },
        "movement_tags": [
            "horizontal_push",
            "shoulder_abduction",
        ],
        "difficulty": "intermediate",
        "unilateral_or_bilateral": "bilateral",
        "estimated_station_time_minutes": 15,
        "default_sets": 4,
        "default_rep_range": "6-10",
    },

    {
        "name": "Pull Up",
        "primary_muscle": "back",
        "secondary_muscles": ["biceps"],
        "equipment_type": "pullup_bar",
        "movement_pattern": "vertical_pull",
        "injury_risk": {
            "shoulder": "medium",
            "elbow": "low",
        },
        "movement_tags": [
            "vertical_pull",
            "elbow_flexion",
        ],
        "difficulty": "intermediate",
        "unilateral_or_bilateral": "bilateral",
        "estimated_station_time_minutes": 10,
        "default_sets": 4,
        "default_rep_range": "6-12",
    },

    {
        "name": "Goblet Squat",
        "primary_muscle": "legs",
        "secondary_muscles": ["glutes", "core"],
        "equipment_type": "dumbbells",
        "movement_pattern": "squat",
        "injury_risk": {
            "knee": "medium",
            "lower_back": "low",
        },
        "movement_tags": [
            "deep_squat",
            "loaded_spine",
        ],
        "difficulty": "beginner",
        "unilateral_or_bilateral": "bilateral",
        "estimated_station_time_minutes": 12,
        "default_sets": 3,
        "default_rep_range": "8-12",
    },
]