from rest_framework import viewsets

from .models import InjuryRecord, UserProfile
from .serializers import (
    InjuryRecordSerializer,
    UserProfileSerializer,
)


from rest_framework.permissions import IsAuthenticated

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

class InjuryRecordViewSet(viewsets.ModelViewSet):
    serializer_class = InjuryRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InjuryRecord.objects.filter(profile__user=self.request.user)