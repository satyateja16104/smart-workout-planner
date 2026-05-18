from rest_framework import viewsets

from .models import BuddyPair
from .serializers import BuddyPairSerializer
from rest_framework.permissions import IsAuthenticated


class BuddyPairViewSet(viewsets.ModelViewSet):
    queryset = BuddyPair.objects.all()
    serializer_class = BuddyPairSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        "filter to only buddy pairs where the user is either host or buddy"
        return BuddyPair.objects.filter(host=self.request.user) | BuddyPair.objects.filter(buddy=self.request.user)