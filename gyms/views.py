from rest_framework import viewsets

from .models import Gym, GymEquipment
from .serializers import (
    GymEquipmentSerializer,
    GymSerializer,
)


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class GymEquipmentViewSet(viewsets.ModelViewSet):
    queryset = GymEquipment.objects.all()
    serializer_class = GymEquipmentSerializer