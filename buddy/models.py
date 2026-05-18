import uuid

from django.conf import settings
from django.db import models

from gyms.models import Gym

from common.constants.choices import BuddyPairStatus
from common.models.base import TimeStampedModel


class BuddyPair(TimeStampedModel):
    host_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="hosted_pairs",
    )

    joined_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="joined_pairs",
        null=True,
        blank=True,
    )

    selected_gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="buddy_pairs",
    )

    invite_code = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
    )

    status = models.CharField(
        max_length=20,
        choices=BuddyPairStatus.choices,
        default=BuddyPairStatus.PENDING,
    )

    compatibility_score = models.FloatField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = str(uuid.uuid4()).replace("-", "")[:12]

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.host_user.username} Buddy Pair"