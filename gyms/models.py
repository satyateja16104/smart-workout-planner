from django.conf import settings
from django.db import models

from common.constants.choices import EquipmentType
from common.models.base import TimeStampedModel


class Gym(TimeStampedModel):
    name = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_gyms",
    )

    def __str__(self):
        return self.name


class GymEquipment(TimeStampedModel):
    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="equipment",
    )

    equipment_type = models.CharField(
        max_length=50,
        choices=EquipmentType.choices,
    )

    quantity = models.PositiveIntegerField(default=1)
    class Meta:
        unique_together = ("gym", "equipment_type")
    def __str__(self):
        return f"{self.gym.name} - {self.equipment_type}"