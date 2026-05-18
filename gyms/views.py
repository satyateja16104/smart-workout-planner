from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Gym, GymEquipment
from .serializers import (
    GymEquipmentSerializer,
    GymSerializer,
)


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GymEquipmentViewSet(viewsets.ModelViewSet):
    queryset = GymEquipment.objects.all()
    serializer_class = GymEquipmentSerializer
    permission_classes = [IsAuthenticated]