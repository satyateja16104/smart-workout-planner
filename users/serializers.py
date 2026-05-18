from rest_framework import serializers

from .models import InjuryRecord, User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
        def create(self, validated_data):
            validated_data["user"] = self.context["request"].user
            return super().create(validated_data)
        def perform_create(self, serializer):
            serializer.save(user=self.request.user)


class InjuryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryRecord
        fields = "__all__"