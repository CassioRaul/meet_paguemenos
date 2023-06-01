from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ManagerSerializer, CollaboratorSerializer
from home import models

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = models.UserManager.objects.all()
    serializer_class = ManagerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.BaseAuthentication]

class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = models.UserCollaborator.objects.all()
    serializer_class = CollaboratorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.BaseAuthentication]
