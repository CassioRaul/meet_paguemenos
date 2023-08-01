from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import FeedbackSerializer #, DeleteFeedbackGSerializer,FeedbackCSerializer, DeleteFeedbackCSerializer
from feedback import models

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset= models.Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes= [permissions.IsAuthenticated]
    # authentication_classes =[authentication.BaseAuthentication]

