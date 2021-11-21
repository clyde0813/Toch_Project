from rest_framework import viewsets
from oneroom.models import *
from .serializer import AttributionSerializer
from rest_framework import viewsets

from oneroom.models import *
from .serializer import AttributionSerializer


class AttributionViewSet(viewsets.ModelViewSet):
    queryset = Attribution.objects.all()
    serializer_class = AttributionSerializer
