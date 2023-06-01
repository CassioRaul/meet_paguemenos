from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .api.viewsets import LogsViewSet

router = routers.DefaultRouter()
router.register(r'', LogsViewSet)

urlpatterns = [
    path('logs/', include(router.urls)),
]
