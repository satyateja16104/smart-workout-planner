from rest_framework import viewsets

from .models import BuddyPair
from .serializers import BuddyPairSerializer


class BuddyPairViewSet(viewsets.ModelViewSet):
    queryset = BuddyPair.objects.all()
    serializer_class = BuddyPairSerializer