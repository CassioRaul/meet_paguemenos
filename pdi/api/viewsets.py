from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PlanningSerializers,PlanningDelSerializers
from pdi import models

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = models.Planning.objects.all()
    serializer_class = PlanningSerializers
    #permission_classes = [permissions.IsAuthenticated]

class PlanningDeleteViewSet(viewsets.ModelViewSet):
    queryset = models.DelPlanning.objects.all()
    serializer_class = PlanningDelSerializers