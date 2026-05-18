import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q

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
            max_attempts = 10
            for _ in range(max_attempts):
                code = str(uuid.uuid4()).replace("-", "")[:12]
                if not BuddyPair.objects.filter(invite_code=code).exists():
                    self.invite_code = code
                    break
            else:
                raise ValueError("Failed to generate unique invite code")

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.joined_user and self.host_user_id == self.joined_user_id:
            raise ValidationError(
                "host_user and joined_user cannot be the same user when joined_user is set."
            )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(joined_user__isnull=True) | ~Q(host_user=F('joined_user')),
                name='buddy_pair_host_and_joined_user_different',
            )
        ]

    def __str__(self):
        return f"{self.host_user.username} Buddy Pair"