from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views
from feedback.api import viewsets as feedbackviewsets

route = routers.DefaultRouter()
route.register(r'', feedbackviewsets.FeedbackViewSet, basename= "feedback")
route.register(r'', feedbackviewsets.DeleteFeedbackViewSet, basename= "delete_feedback")

urlpatterns = [
    path('feedback', include(route.urls)),
    path('delete_feedback', include(route.urls)),
]
