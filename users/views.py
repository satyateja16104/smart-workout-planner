from rest_framework import viewsets

from .models import InjuryRecord, UserProfile
from .serializers import (
    InjuryRecordSerializer,
    UserProfileSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class InjuryRecordViewSet(viewsets.ModelViewSet):
    queryset = InjuryRecord.objects.all()
    serializer_class = InjuryRecordSerializer