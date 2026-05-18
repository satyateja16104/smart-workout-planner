from rest_framework import serializers

from .models import Gym, GymEquipment


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


class GymEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymEquipment
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]