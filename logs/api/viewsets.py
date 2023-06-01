from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import LogsSerializer
from logs.models import Logs

class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.BaseAuthentication]
