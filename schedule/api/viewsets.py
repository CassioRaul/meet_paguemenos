from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ScheduleSerializers, ScheduleDelSerializers
from schedule import models

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = ScheduleSerializers
    # permission_classes = [permissions.IsAuthenticated] #Isso aqui é basicamente uma autenticação de token para o usuario, ele comentado o usuario pode acessar

class ScheduleDeleteSerializersViewSet(viewsets.ModelViewSet):
    queryset = models.DelSchedule.objects.all()
    serializer_class = ScheduleDelSerializers
    # permission_classes = [permissions.IsAuthenticated]