from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PlanningSerializers
from pdi import models

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = models.Planning.objects.all()
    serializer_class = PlanningSerializers
    #permission_classes = [permissions.IsAuthenticated]
