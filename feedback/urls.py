from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views
from feedback.api import viewsets as feedbackviewsets

route_feedbackg = routers.DefaultRouter()
route_feedbackg.register(r'', feedbackviewsets.FeedbackViewSet)

urlpatterns = [
    path('feedback/', include(route_feedbackg.urls)),
]