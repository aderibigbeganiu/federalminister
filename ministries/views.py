from rest_framework import viewsets
from .models import Ministries
from .serializers import MinistriesSerializer

class MinistriesViewSet(viewsets.ModelViewSet):
    queryset = Ministries.objects.all()
    serializer_class = MinistriesSerializer
    lookup_field = 'pk'