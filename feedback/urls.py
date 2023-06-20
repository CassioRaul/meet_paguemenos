from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views
from feedback.api import viewsets as feedbackviewsets

route_feedback = routers.DefaultRouter()
route_feedback.register(r'', feedbackviewsets.FeedbackViewSet)

# route_del_feedback = routers.DefaultRouter()
# route_del_feedback.register(r'', feedbackviewsets.DeleteFeedbackViewSet)

urlpatterns = [
    path('feedback/', include(route_feedback.urls)),
    # path('delete_feedback/', include(route_del_feedback.urls)),
]
