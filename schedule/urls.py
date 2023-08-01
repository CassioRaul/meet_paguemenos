from . import views
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from schedule.api import viewsets as scheduleviewsets
from schedule.api import viewsets as scheduleseleteserializerssiewset

route_schedule = routers.DefaultRouter()
route_schedule.register(r'', scheduleviewsets.ScheduleViewSet)


urlpatterns = [
    path('schedule/', include(route_schedule.urls)),
]
