from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views
from feedback.api import viewsets as feedbackviewsets

route_feedbackg = routers.DefaultRouter()
route_feedbackg.register(r'', feedbackviewsets.FeedbackGViewSet)

route_del_feedbackg = routers.DefaultRouter()
route_del_feedbackg.register(r'', feedbackviewsets.DeleteFeedbackGViewSet)

route_feedbackc = routers.DefaultRouter()
route_feedbackc.register(r'', feedbackviewsets.FeedbackCViewSet)

route_del_feedbackc = routers.DefaultRouter()
route_del_feedbackc.register(r'', feedbackviewsets.DeleteFeedbackCViewSet)


urlpatterns = [
    path('feedbackg/', include(route_feedbackg.urls)),
    path('delete_feedbackg/', include(route_del_feedbackc.urls)),
    path('feedbackc/', include(route_feedbackc.urls)),
    path('delete_feedbackc/', include(route_del_feedbackc.urls)),
]
