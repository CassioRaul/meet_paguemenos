from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import FeedbackSerializer #, DeleteFeedbackGSerializer,FeedbackCSerializer, DeleteFeedbackCSerializer
from feedback import models

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset= models.Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes= [permissions.IsAuthenticated]
    # authentication_classes =[authentication.BaseAuthentication]

# class DeleteFeedbackGViewSet(viewsets.ModelViewSet):
#     queryset= models.DeleteFeedbackG.objects.all()
#     serializer_class = DeleteFeedbackGSerializer
    # permission_classes= [permissions.IsAuthenticated]
    # authentication_classes =[authentication.BaseAuthentication]
    
# class FeedbackCViewSet(viewsets.ModelViewSet):
#     queryset= models.FeedbackC.objects.all()
#     serializer_class = FeedbackCSerializer
    # permission_classes= [permissions.IsAuthenticated]
    # authentication_classes =[authentication.BaseAuthentication]

# class DeleteFeedbackCViewSet(viewsets.ModelViewSet):
#     queryset= models.DeleteFeedbackC.objects.all()
#     serializer_class = DeleteFeedbackCSerializer
    # permission_classes= [permissions.IsAuthenticated]
    # authentication_classes =[authentication.BaseAuthentication]