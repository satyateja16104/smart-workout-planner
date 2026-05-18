from django.core.exceptions import ValidationError

from common.constants.injury_tags import (
    APPROVED_INJURY_TAGS,
)


VALID_TAGS = set(APPROVED_INJURY_TAGS)


def validate_injury_tags(value):
    if not isinstance(value, list):
        raise ValidationError(
            "Movement tags must be a list."
        )

    invalid_tags = [
        tag
        for tag in value
        if tag not in VALID_TAGS
    ]

    if invalid_tags:
        raise ValidationError(
            f"Invalid movement tags: {invalid_tags}"
        )