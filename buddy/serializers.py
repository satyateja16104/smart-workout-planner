from rest_framework import serializers

from .models import BuddyPair


class BuddyPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuddyPair
        fields = "__all__"