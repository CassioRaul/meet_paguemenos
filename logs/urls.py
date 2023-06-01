from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .api.viewsets import LogsViewSet

route_logs = routers.DefaultRouter()
route_logs.register(r'', LogsViewSet)

urlpatterns = [
    path('logs/', include(route_logs.urls)),
]
